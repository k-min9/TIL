'''
pyinstaller main.py --onefile --noconsole --hidden-import=urllib.request
pyinstaller main.py --onefile --hidden-import=urllib.request
'''
import urllib.request

url = 'https://github.com/k-min9/m9assistant/releases/download/proto/Install.bat'
save_path = 'Install.bat'

url = 'https://huggingface.co/spaces/zomehwh/vits-models/resolve/main/pretrained_models/mika/mika.pth'
save_path = 'mika.pth'

urllib.request.urlretrieve(url, save_path)
print(f'Downloaded: {url} => {save_path}')
