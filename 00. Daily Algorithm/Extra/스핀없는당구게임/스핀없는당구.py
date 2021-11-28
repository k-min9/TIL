import socket
import time
from math import radians, degrees, atan2, dist, cos, sin

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_KANGMINGU'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send(('%d/%d' % (CODE_REQUEST, CODE_REQUEST)).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = float(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %f, %f' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    # 상수
    # BALL_SIZE = 5.73
    BALL_SIZE = 5.5
    BALL_RADIUS = BALL_SIZE/2    

    

    angle = 0.0
    power = 0.0

    def get_angle(start, end):
        return degrees(atan2((end[1]-start[1]), (end[0]-start[0]))) % 360
    
    def get_target_point(target, hole):
        angle_hole = get_angle(target, hole)
        x = target[0] + BALL_SIZE * cos(radians(180 + angle_hole))
        y = target[1] + BALL_SIZE * sin(radians(180 + angle_hole))
        try:
            print('tp', HOLES.index(hole), angle_hole, x, y)
        except:
            print('tp', angle_hole, x, y)
        return x, y

    def get_cos(white, tp, hole):
        return cos(radians(get_angle(white, tp)) - radians(get_angle(tp, hole)))

    def check_obstacle(start, end):
        sx = start[0]
        sy = start[1]
        ex = end[0]
        ey = end[1]
        theta = atan2((ey-sy), (ex-sx))
        x = sx
        y = sy
        # 조사대상 제외 = target 공과 흰 공
        check_data = gameData.balls[1:]
        if [sx, sy] in gameData.balls[1:]:
            check_data.remove([sx, sy])
            # print('YES')
        print('chk_ball Origin : ', check_data)
        while dist((x, y), (ex, ey)) > BALL_RADIUS and check_data:
            # 충돌 판정
            flag = False
            for ball in check_data:
                if dist((x, y), ball) <= BALL_SIZE:
                    # 충돌 발생
                    flag = True
                    print('충돌종류 : ', (sx, sy), (ex, ey))
                    print('충돌지점 : ', (x, y))
                    break
            if flag:
                # 충돌 있습니다.
                return True
            # 탐지기 전진
            x += (BALL_RADIUS/10) * cos(theta)
            y += (BALL_RADIUS/10) * sin(theta) 
            #print('더미좌표:', x, y)
        else:
            # 충돌 없습니다.
            return False

    # 흰 공 좌표 리스트
    white = gameData.balls[0]

    # 선공(1) 후공(2)        
    if gameData.order == 1: 
        target_lists = [1, 3]
    else:
        target_lists = [2, 4]
    target_balls = list()
    for target in target_lists:
        if gameData.balls[target][0] != -1: # y축 생략
            target_balls.append(target)
    # 목적구 다 들어갔는데 게임이 안 끝남 = 남은 타겟은 8번
    if not target_balls:
        target_balls = [5]
    #print(target_balls)

    # 공 기준으로 위치 작성
    target_points = list()
    for target in target_balls:
        target_points.append((gameData.balls[target][0], gameData.balls[target][1]))
    #print(target_points)

    # 여기서부터 시작
    answer = [0, 0]
    max_cos = -1
    for hole in HOLES:
        for target_point in target_points:
            tx, ty = get_target_point(target_point, hole)
            if check_obstacle(white, (tx, ty)) or check_obstacle(target_point, hole):
                continue

            # 진입각 발사각 비교
            temp_cos = get_cos(white, (tx, ty), hole)
            print(temp_cos)
            if temp_cos > max_cos:
                max_cos = temp_cos
                answer = [tx, ty]
                power = dist(white, answer) + dist(answer, hole)
   
    print('---')
    print(answer)
    print('---')

    # 노 쿠션 클린 힛 가능?
    if answer == [0, 0]:
        answer = [gameData.balls[target_balls[0]][0], gameData.balls[target_balls[0]][1]]
        power = 100
    angle = (90 - get_angle(white, answer)) % 360
    print('final', answer, power)
    power = min(100, power * 0.33)
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()
