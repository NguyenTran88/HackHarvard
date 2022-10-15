import argparse
import utils


def main():
    f = open('.api-key', 'r')
    API_KEY = f.readline()[:-1]

    HEADER = {
        'authorization': API_KEY,
        'content-type': 'application/json'
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('audio_file', nargs='?', help='url to file or local audio filename')
    parser.add_argument('--local', action='store_true', help='must be set if audio_file is a local filename')
    parser.add_argument('--id', action='store', help='provide previous transcript id (not text)')

    args = parser.parse_args()

    if not (args.id or args.local or args.audio_file):
        print('Please provide at least 1 argument - check README for usage instructions.')
        return

    if args.id:
        polling_endpoint = utils.make_polling_endpoint({'id': args.id})
    else:
        if args.local:
            # Upload the audio file to AssemblyAI
            upload_url = utils.upload_file(args.audio_file, HEADER)
        else:
            upload_url = {'upload_url': args.audio_file}

        json = {
            'audio_url': upload_url['upload_url'],
            "content_safety": True
        }

        # Request a transcription
        json_response = utils.json_request(json, HEADER)

        # Create a polling endpoint that will let us check when the transcription is complete
        polling_endpoint = utils.make_polling_endpoint(json_response)

    # Wait until the transcription is complete
    polling_response = utils.wait_for_completion(polling_endpoint, HEADER)

    content_safety_labels = polling_response['content_safety_labels']

    print('Content Safety Labels:')
    print(content_safety_labels)

    # # Request the paragraphs of the transcript
    # paragraphs = utils.get_paragraphs(polling_endpoint, HEADER)

    # # Save and print transcript
    # with open('transcript.txt', 'w') as f:
    #     for para in paragraphs:
    #         print(para['text'] + '\n')
    #         f.write(para['text'] + '\n')

    return


if __name__ == '__main__':
    main()
