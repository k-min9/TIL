'''
ogg > wav 로 변환해보기
'''
import os
from pydub import AudioSegment

AudioSegment.converter = os.path.abspath('.\\ffmpeg\\bin\\ffmpeg.exe')

def batch_ogg_to_wav(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".ogg"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".wav")
            audio = AudioSegment.from_ogg(input_file)
            audio.export(output_file, format='wav')

input_folder = 'audio_converter_input'  # 입력 폴더 경로
output_folder = 'audio_converter_output'  # 출력 폴더 경로

batch_ogg_to_wav(input_folder, output_folder)
