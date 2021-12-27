var socket = io()

// 클라이언트 쪽
/* on : 수신 함수 */
/* 접속 되었을 때 실행 */
socket.on('connect', function() {
  // 접속시 이름 입력 받기
  var name = prompt('반갑습니다!', '')

  // 이름 빈칸인 경우
  if (!name) {
    name = '익명'
  }

  // 서버에 새로운 유저가 온것을 알림
  socket.emit('newUser', name)
})

socket.on('update', function(data) {
  console.log(`${data.name}: ${data.message}`)
})

/* emit : 전송 함수 */
function send() {
  // 입력되어있는 데이터 가져오기
  var message = document.getElementById('test').value
  
  // 가져왔으니 데이터 빈칸으로 변경
  document.getElementById('test').value = ''

  // 서버로 send 이벤트 전달 + 데이터와 함께 -> .on('send') 즉 이벤트 명이 동일한 쪽이 수령함
  socket.emit('message', {type: 'message', message: message})
}
