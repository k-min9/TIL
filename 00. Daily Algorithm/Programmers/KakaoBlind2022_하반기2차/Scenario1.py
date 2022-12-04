'''
카카오 채용 끝나고 대충 엠바고 풀렸을테니 업로드. 
최종버전은 아니었던걸로 기억하는데 일단 이 상태로도 2차 통과

전략 : Best Fit
시나리오 1 : problem: 1, H : 3, W : 20, DAY = 200
'''
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
        # if self.verbose:
        #     print(response.status_code)
        return response.json()
    
    def get(self, x, headers=None, params=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.get(url, headers=headers, params=params)
        # if self.verbose:
        #     print(response.status_code)
        return response.json()
    
    def put(self, x, headers=None, data=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.put(url, headers=headers, data=data)
        # if self.verbose:
        #     print(response.status_code)
        return response.json()


# 객실번호(AABBB) -> 층, 호수
def roomnum_to_hw(room_num):
    h = int(room_num) // 1000 - 1
    w = int(room_num) % 1000 - 1
    return h, w


# 층, 호수 -> 객실번호(AABBB)
def hw_to_roomnum(h, w):
    h += 1
    w += 1
    h = str(h)
    w = str(w)
    w = '0'*(3-len(w)) + w
    return h + w


# 호텔 체크 인 (체크아웃 날짜, 시작 h, 시작 w, 예약 방 수)
def hotel_checkin(day, h, w, room_len):
    # 혹시 모르니 체크...? << 고려중
    W = len(rooms[0])
    if w + room_len - 1 > W:
        print('체크인 오류 발생')
        return

    for i in range(room_len):
        rooms[h][w+i] = day


# 호텔 체크 아웃 
def hotel_checkout(day):
    H = len(rooms)
    W = len(rooms[0])
    for h in range(H):
        for w in range(W):
            if rooms[h][w] == day:
                rooms[h][w] = 0


# 현재 가장 긴 연속 길이와 시작 호수 (Worst_fit용)
def hotel_available():
    H = len(rooms)
    W = len(rooms[0])
    ret = 0
    retH = 0
    retW = 0
    for h in range(H):
        tmp = 0
        tmpH = h
        tmpW = 0
        for w in range(W):
            if rooms[h][w] == 0:
                tmp += 1
            else:
                if tmp > ret:
                    ret = tmp
                    ret = h
                    retH = tmpH
                    retW = tmpW
                tmp = 0
                tmpH = h
                tmpW = w + 1
        ret = max(ret, tmp)
    return ret, retH, retW


# 현재 비어있는 호텔 길이와 호수 전부 리턴 (First fit, Best fit용)
def hotel_info():
    ret = set()
    H = len(rooms)
    W = len(rooms[0])
    for h in range(H):
        tmp = 0
        tmpH = h
        tmpW = 0
        for w in range(W):
            if rooms[h][w] == 0:
                tmp += 1
            else:
                if tmp != 0:
                    ret.add((tmp, tmpH, tmpW))
                tmp = 0
                tmpW = w+1
        ret.add((tmp, tmpH, tmpW))
    ret = list(ret)
    ret.sort()
    return ret


if __name__ == "__main__":
    problem = 1  # 시나리오 번호
    H = 3
    W = 20
    MAX_DATE = 200

    X = 8  # 너무 지나치게 빠른 요청 제어 변수

    token = 'da395300a102c9692d2708e53395645b'
    base_url = f'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'
    
    parser = Parser(token=token, base_url=base_url, verbose=1)
    post_headers = {
        'X-Auth-Token': parser.token,
        'Content-Type': parser.content_type,
    }

    # 문제 진행용 auth_key 받기
    start_res = parser.post('/start', headers=post_headers, data=json.dumps({'problem': problem}))
    auth_key = start_res['auth_key']
    print('auth_key', auth_key)

    headers = {
        'Authorization': auth_key,
        'Content-Type': parser.content_type,
    }

    # 호텔 건설
    rooms = [[0]*W for _ in range(H)]
    request_waiting = list()  # 답변을 기다리는 예약 요청 (방 길이-내림, 답변 기한 - 오름, 시작 날짜, 끝나는 날짜, id)
    request_waiting2 = list()  # 너무 빠른 예약이라고 판단되는 요청들 (시작 날짜-오름, 끝나는 날짜, 방 길이, id), 관련 변수 : X
    assign_waiting = list()  # 예약이 끝나서(이 시점에 배정해버림) 당일이 되면 실제로 예약할 요청들 (시작 날짜-오름, 방 번호, id)


    for d in range(MAX_DATE):
        # 오늘 날짜(가독성)
        now_date = d+1        
        hotel_checkout(now_date)  # 로컬 방 정보 갱신(체크아웃)

        # 오늘 들어온 새로운 예약 요청 받아오기
        new_request_res = parser.get('/new_requests', headers=headers)
        for res in new_request_res['reservations_info']:
            id = res['id']
            amount = res['amount']
            check_in_date = res['check_in_date']
            check_out_date = res['check_out_date']

            # 너무 빠른 예약은 > request_waiting2에 대기, 그 외 심사 대상은 request_waiting
            if now_date + X > check_in_date or now_date + X > 200:
                # request_waiting : (방 길이-내림, 답변 기한 - 오름, 시작 날짜, 끝나는 날짜, id)
                request_waiting.append((amount, min(now_date+14, check_in_date-1) ,check_in_date, check_out_date, id))
            else:
                # request_waiting2 : (시작 날짜-오름, 끝나는 날짜, 방 길이, id)
                request_waiting2.append((check_in_date, check_out_date, amount, id))

        # 기존 request_waiting2를 request_waiting으로 보낼지 판단
        for check_in_date, check_out_date, amount, id in request_waiting2[:]:
            if now_date + X > check_in_date or now_date + X > 200:
                request_waiting.append((amount, min(now_date+14, check_in_date-1) ,check_in_date, check_out_date, id))
                request_waiting2.remove((check_in_date, check_out_date, amount, id))

        # 기한이 지나버린 request_waiting, Refused 했을때 점수상 이점이 없음을 확인
        for amount, deadline, check_in_date, check_out_date, id in request_waiting[:]:
            if deadline < now_date:
                request_waiting.remove((amount, deadline, check_in_date, check_out_date, id))

        # 객실 수가 많은 요청을 최대한 우선적으로 수용하게 sort
        request_waiting.sort(key=lambda x: (-x[0], x[1]))

        # 현재 local 호텔 정보 가져오기
        rooms_info = hotel_info()
        rooms_info.sort()

        # BEST FIT + 예약 요청 응답하기
        replies = list()  # 형태 : [{'id':867284, 'reply':'accepted'}, { 'id': 986323, 'reply': 'accepted'}]
        for amount, deadline, check_in_date, check_out_date, id in request_waiting[:]:
            for available, h, w in rooms_info:
                if amount <= available:
                    hotel_checkin(check_out_date, h, w, amount)
                    replies.append({'id':id, 'reply':'accepted'})
                    assign_waiting.append((check_in_date, hw_to_roomnum(h, w), id))
                    request_waiting.remove((amount, deadline, check_in_date, check_out_date, id))
                    break
            # 재정비
            rooms_info = hotel_info()
            rooms_info.sort()
        reply_res = parser.put('/reply', headers=headers, data=json.dumps({'replies': replies}))    


        # 방 배정 + 하루 진행하기
        assigns = list()  # 형태 : [{'id':867284, 'room_number':'1001'}, {'id':986323, 'room_number':'2001'}]
        for start_date, room_num, id in assign_waiting[:]:
            if start_date == now_date:
                assigns.append({'id':id, 'room_number': room_num})
                assign_waiting.remove((start_date, room_num, id))
        sim_res = parser.put('/simulate', headers=headers, data=json.dumps({'room_assign': assigns}))   
        # print(sim_res) # res : 1일 증가한 현재 날짜, 예약은 승낙했으나 배정에 실패한 횟수

        ## 상황 모니터링 용 함수
        print('day', now_date)
        # print('hotel ' + str(now_date), rooms)
        # print(min(rooms))

    # 스코어 체크
    score_res = parser.get('/score', headers=headers)
    print(score_res)
