

import sys
import time
import requests

API_KEY = "3a48a513f73840e5b34ae910611ff736"
HEADERS = {"Authorization": API_KEY}
TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"
audio_file = sys.argv[1]
output_name = input("Enter the name for the output text file ") + ".txt"


def upload_file(file_path, chunk_size=5242880):
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def start_transcription(file_name):
    upload_resp = requests.post(
        "https://api.assemblyai.com/v2/upload",
        headers=HEADERS,
        data=upload_file(file_name)
    ).json()
    audio_url = upload_resp["upload_url"]

    trans_resp = requests.post(
        TRANSCRIPT_URL,
        json={"audio_url": audio_url},
        headers=HEADERS
    ).json()

    return trans_resp["id"]


def wait_for_completion(transcript_id, interval=5):
    status = None
    while True:
        resp = requests.get(
            f"{TRANSCRIPT_URL}/{transcript_id}", headers=HEADERS).json()
        status = resp.get("status")

        if status == "completed":
            return resp

        if status == "error":
            raise RuntimeError(
                f"Transcription failed: {resp.get('error', '<no message>')}")

        print(f"Status is '{status}', waiting {interval}s before retrying…")
        time.sleep(interval)


transcript_id = start_transcription(audio_file)
final_result = wait_for_completion(transcript_id, interval=5)

with open(output_name, 'w') as f:
    f.write(final_result['text'])
print(f"Transcription saved to {output_name}")
