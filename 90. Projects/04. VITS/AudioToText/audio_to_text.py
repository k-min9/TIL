import os
from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def transcribe_speech(file_path):
    client = speech.SpeechClient()

    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=22050,
        language_code="ja-JP",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcript = result.alternatives[0].transcript
        transcripts.append(transcript)

    return " ".join(transcripts)

input_folder = "input"
output_file = "result.txt"
prefix= "datasets/frieza/"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            file_path = os.path.join(input_folder, filename)
            result = transcribe_speech(file_path)
            print("Filename:", filename)
            print("Result:", result)
            print()

            # 결과를 텍스트 파일에 저장
            f.write(prefix+filename+"|"+result+"\n")
