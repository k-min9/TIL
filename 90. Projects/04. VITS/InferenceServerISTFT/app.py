from flask import Flask, request, send_file
import io
from werkzeug.serving import WSGIRequestHandler

import torch

import commons
import utils
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence

from scipy.io.wavfile import write

app = Flask(__name__)

# 초기화
hps = utils.get_hparams_from_file("./data/ljs_mb_istft_vits.json")

net_g = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    **hps.model)#.cuda()
_ = net_g.eval()
_ = utils.load_checkpoint("./data/G_5300.pth", net_g, None)

# 초기 로딩 함수
# @app.before_first_request
# def setup():
#     pass

def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm

def get_audio(text):
    stn_tst = get_text(text, hps)
    with torch.no_grad():
        #x_tst = stn_tst.cuda().unsqueeze(0)
        x_tst = stn_tst.unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)])#.cuda()
        audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=0.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
    return audio


# 일본어 텍스트를 입력받아 변환
@app.route('/getSound/jp/')
@app.route('/getSound/jp/<text>')
def synthesize(text=None):
    if text is None:
        text = 'こんにちは'
        # text = "すみません…できればでいいのですが、わたしについできてください。"
    audio = get_audio(text)

    # output_file = io.BytesIO()
    write('./output.wav', hps.data.sampling_rate, audio)
    # output_file.seek(0)
    # return send_file('./output.wav', mimetype="audio/wav", as_attachment=True, download_name="output.wav")
    return send_file('./output.wav', mimetype="audio/wav")


if __name__ == "__main__" :
    # app.run(host='127.0.0.1', port=8080, debug=True)
    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    app.run(host='0.0.0.0')