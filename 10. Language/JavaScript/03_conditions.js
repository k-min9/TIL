/*
  [if문 연습]
    username 변수의 값에 따라 다른 메세지를 출력
  - 관리자(admin)일 경우 "관리자님 환영합니다."
  - 매니저(manager)일 경우 "매니저님 환영합니다."
  - 그 외 모든 경우 "{username}님 환영합니다"
*/

const username = 'admin'

if (username === 'admin') {
  console.log('관리자님 환영합니다.')
} else if (username === 'manager') {
  console.log('매니저님 어서오세요.')
} else {
  console.log(`${username} 어서오고`)
}


/*
  [switch문 연습]

  operator 변수의 값에 따라 다른 계산을 하는 조건을 작성하세요.
  - '+'는 두 숫자의 합을 출력합니다.
  - '-'는 두 숫자의 차이를 출력합니다.
  - '*'는 두 숫자의 곲을 출력합니다.
  - '/'는 두 숫자의 나눗셈 결과를 출력합니다.
  - 만약 위 4가지 경우에 해당하지 않는 operator라면,
    "유효하지 않은 연산자입니다."라는 메세지를 출력하세요.
*/

const numOne = 10
const numTwo = 100
let operator = '+'

switch (operator) {
  case '+': {
    console.log(numOne + numTwo)
    break
  }
  case '-': {
    console.log(numOne - numTwo)
    break
  }
  case '*': {
    console.log(numOne * numTwo)
    break
  }
  case '/': {
    console.log(numOne / numTwo)
    break
  }
  default: {
    console.log('invalid operator')
  }
}