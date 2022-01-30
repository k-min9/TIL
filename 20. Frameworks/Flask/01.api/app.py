from flask import Flask, Response, jsonify, make_response

app = Flask(__name__) 


# pathvariable 받기
@app.route("/num/<tid>")
def response_test(tid):
    # 내용물, response_num, 헤더 추가 내용물
    res = Response("내용", 200, {'test': 'what'})
    res2 = Response(tid, 200, {'test': 'what'})
    return make_response(res2)

# build 하는 느낌의 Response
@app.route("/num2/<tid>")
def response_test2(tid):
    res = Response("Test")
    res.headers.add('Auth', 'token')
    res.set_data("이거가 json안에 들어가나?")  # 스프링 반환
    # res.set_cookie("key", "value")  # 안쓰겠지 싶긴 함
    return make_response(res)

# json 반환    
@app.route("/num3/<tid>")
def response_test3(tid):
    data = dict()
    data[0] = 1
    data[1] = tid

    return jsonify(data)



@app.route("/test") 
def hello():
    return "Hello World!"

if __name__ == "__main__" :
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0')

