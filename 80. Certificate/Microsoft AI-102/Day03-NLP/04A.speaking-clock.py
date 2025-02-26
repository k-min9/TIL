'''
pip install python-dotenv
pip install azure-cognitiveservices-speech==1.30.0
pip install playsound==1.2.2

흔한 STT, TTS
'''
from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = 'eastus'  # 배포지역

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print('Ready to use speech service in:', speech_config.region)
        
        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

# 음성인식 구성
def TranscribeCommand():
    command = ''

    # Configure speech recognition (기본 시스템 마이크 음성인식 사용시...)
    # audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    # speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    # print('Speak now...')
    
    # Configure speech recognition
    from playsound import playsound
    current_dir = os.getcwd()
    audioFile = current_dir + '\\time.wav'
    playsound(audioFile)
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    
    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

# 호출된 함수로 답변을 읽어 줌
def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
        

    # # Synthesize spoken output
    # speak = speech_synthesizer.speak_text_async(response_text).get()
    # if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
    #     print(speak.reason)
        
    # Synthesize spoken output (SSML로 포맷 지정 가능 / 목소리라던가, 대화 추가 가능)
    responseSsml = " \
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
            <voice name='en-GB-LibbyNeural'> \
                {} \
                <break strength='weak'/> \
                Time to end this lab! \
            </voice> \
        </speak>".format(response_text)
    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()