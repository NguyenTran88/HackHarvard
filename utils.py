import requests
import time


UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"


def convert_ms_to_time(ms):
    mins = str(ms // 60000).zfill(2)
    secs = str(round((ms % 60000) / 1000, 2)).zfill(4)
    time = f'{mins}:{secs}'
    return time


# Helper for `upload_file()`
def _read_file(filename, chunk_size=5242880):
    with open(filename, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


# Uploads a file to AAI servers
def upload_file(audio_file, header):
    upload_response = requests.post(
        UPLOAD_ENDPOINT,
        headers=header, data=_read_file(audio_file)
    )
    return upload_response.json()


# Request transcript for file uploaded to AAI servers
def json_request(json, header):
    json_response = requests.post(
        TRANSCRIPT_ENDPOINT,
        json=json,
        headers=header
    )
    return json_response.json()


# Make a polling endpoint
def make_polling_endpoint(json_response):
    polling_endpoint = "https://api.assemblyai.com/v2/transcript/"
    polling_endpoint += json_response['id']
    return polling_endpoint


# Wait for the transcript to finish
def wait_for_completion(polling_endpoint, header):
    while True:
        polling_response = requests.get(polling_endpoint, headers=header)
        polling_response = polling_response.json()

        if polling_response['status'] == 'completed':
            return polling_response
            break

        time.sleep(5)


# Get the paragraphs of the transcript
def get_paragraphs(polling_endpoint, header):
    paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=header)
    paragraphs_response = paragraphs_response.json()

    paragraphs = []
    for para in paragraphs_response['paragraphs']:
        paragraphs.append(para)

    return paragraphs
