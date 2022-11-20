import requests
import json

class Parser(object):
    def __init__(self, token: str, base_url: str, verbose=0):
                
        if base_url[-1] == '/':
            base_url = base_url[:-1]
        self.base_url = base_url
        self.content_type = 'application/json'
        self.token = token
        self.verbose = verbose

    def post(self, x, headers=None, data=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.post(url, headers=headers, data=data)
        if self.verbose:
            print(response.status_code)
        return response.json()
    
    def get(self, x, headers=None, params=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.get(url, headers=headers, params=params)
        if self.verbose:
            print(response.status_code)
        return response.json()
    
    def put(self, x, headers=None, data=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.put(url, headers=headers, data=data)
        if self.verbose:
            print(response.status_code)
        return response.json()

token = 'bf18c716d554e6dc7cf0b7eb86e35e57'
base_url = f'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
problem = 1  # 시나리오 번호
parser = Parser(token=token, base_url=base_url, verbose=1)
post_headers = {
    'X-Auth-Token': parser.token,
    'Content-Type': parser.content_type,
}

start_res = parser.post('/start', headers=post_headers, data=json.dumps({'problem': 1}))
auth_key = start_res['auth_key']

headers = {
    'Authorization': auth_key,
    'Content-Type': parser.content_type,
}
waiting_res = parser.get('/waiting_line', headers=headers)
print(waiting_res)
game_res = parser.get('/game_result', headers=headers)
print(game_res)
# sim_res = parser.put('/simulate', headers=headers, data=json.dumps({'commands': [{'truck_id': 0, 'command': [2, 5, 4, 1, 6]}]}))
match_res = parser.put('/match', headers=headers, data=json.dumps({'pairs': [[1, 2], [9, 7], [11, 49]]}))
print(match_res)
score_res = parser.get('/score', headers=headers)
print(score_res)