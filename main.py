import argparse
from bcolors import bcolors
from matplotlib import pyplot as plt
import utils

USE_COLORS = True


def process_content_safety_labels(content_safety_labels, bad_labels=['crime_violence', 'hate_speech'], f = lambda a, b: a*b, cutoff=0.36):
    aggregate = { label: [] for label in bad_labels }

    results = content_safety_labels['results']
    for result in results:
        labels = result['labels']
        text = result['text']
        timestamp = result['timestamp']
        start, end = timestamp['start'], timestamp['end']
        start, end = utils.convert_ms_to_time(start), utils.convert_ms_to_time(end)

        for label in labels:
            if label['label'] in bad_labels:
                confidence = float(label['confidence'])
                severity = float(label['severity'])

                if USE_COLORS:
                    print(f'Label {bcolors.OKGREEN}{label["label"]}{bcolors.ENDC} found from {bcolors.HEADER}{start}{bcolors.ENDC} to {bcolors.HEADER}{end}{bcolors.ENDC}')
                    print(f'with confidence {bcolors.OKCYAN}{confidence}{bcolors.ENDC} and severity {bcolors.OKCYAN}{severity}{bcolors.ENDC}')
                else:
                    print(f'From {start} to {end}')
                    print(f'with confidence {confidence} and severity {severity}')

                print(text)

                if f(confidence, severity) > cutoff:
                    if USE_COLORS:
                        print(f'{bcolors.WARNING}FLAGGED AS DANGEROUS{bcolors.ENDC}')
                    else:
                        print(f'FLAGGED AS DANGEROUS')

                aggregate[label['label']].append((confidence, severity))
                print()

    return aggregate


def process_sentiment_analysis_results(sentiment_analysis_results):
    total_time = 0
    negative_time = 0
    weighted_negative_time = 0
    times = [0]
    sentiments = [0]
    for sentence in sentiment_analysis_results:
        start, end = sentence['start'], sentence['end']
        times.append(start)
        times.append(end)
        if sentence['sentiment'] == 'POSITIVE':
            sentiments.append(sentiments[-1])
            sentiments.append(sentiments[-1] + sentence['confidence'])
        elif sentence['sentiment'] == 'NEGATIVE':
            sentiments.append(sentiments[-1])
            sentiments.append(sentiments[-1] - sentence['confidence'])
        else:
            sentiments.append(sentiments[-1])
            sentiments.append(sentiments[-1])

        # sentiments.append(sentence['sentiment'])
        total_time += sentence['end'] - sentence['start']
        if sentence['sentiment'] == 'NEGATIVE':
            negative_time += sentence['end'] - sentence['start']
            weighted_negative_time += sentence['confidence'] * (sentence['end'] - sentence['start'])
            print(f'{bcolors.OKGREEN}NEGATIVE{bcolors.ENDC} speech found from {bcolors.HEADER}{utils.convert_ms_to_time(sentence["start"])}{bcolors.ENDC} to {bcolors.HEADER}{utils.convert_ms_to_time(sentence["end"])}{bcolors.ENDC}')
            print('Confidence:', sentence['confidence'])
            print(sentence['text'])
            print()

    return (total_time, negative_time, weighted_negative_time, times, sentiments)

def main():
    f = open('.api-key', 'r')
    API_KEY = f.readline().strip()

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
            "content_safety": True,
            "sentiment_analysis": True,
        }

        # Request a transcription
        json_response = utils.json_request(json, HEADER)

        # Create a polling endpoint that will let us check when the transcription is complete
        polling_endpoint = utils.make_polling_endpoint(json_response)

    # Wait until the transcription is complete
    polling_response = utils.wait_for_completion(polling_endpoint, HEADER)

    content_safety_labels = polling_response['content_safety_labels']
    sentiment_analysis_results = polling_response['sentiment_analysis_results']

    print('<h4>Content Safety Summary:</h4>')
    process_content_safety_labels(content_safety_labels)
    print()

    print('<h4>Sentiment Analysis Summary:</h4>')
    total_time, negative_time, weighted_negative_time, times, sentiments = process_sentiment_analysis_results(sentiment_analysis_results)
    total_time = int(total_time)
    negative_time = int(negative_time)
    weighted_negative_time = int(weighted_negative_time)
    print(f'Negative / Total time of speech: {utils.convert_ms_to_time(negative_time)}/{utils.convert_ms_to_time(total_time)} ({100*round(negative_time / total_time, 4)}%)')

    plt.plot(times, sentiments, '-')
    plt.savefig('result.png')
    # print(times)
    # print(sentiments)

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
