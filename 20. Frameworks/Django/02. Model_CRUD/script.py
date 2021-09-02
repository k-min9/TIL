import requests


for i in range(31, 40):
    url = f'http://127.0.0.1:8000/articles/{i}/delete/'
    requests.post(url)

