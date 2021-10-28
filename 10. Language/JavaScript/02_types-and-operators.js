/*
  [Number 타입 연습]

  JS Number 타입에는
  1. 정수
  2. 실수
  3. Inifinity (= 1/0)
  4. NaN => Not a Number (= 0/0)
*/

// 2시간 30분
const hour = 2 * 60 * 60
const minute = 30 * 60
const curTime = hour + minute

console.log(curTime)

/*
  [String 타입 연습]
*/

// String 이어 붙이기
let username = '유태영'
const message = '안녕하세요!'

username = username + message
console.log(username)

username += message
console.log(username)


//템플릿 리터럴(Template Literal) 활용 예시) 조회수 500회
const viewCnt = 500
console.log('조회수 ' + viewCnt)
console.log(`조회수 ${viewCnt}`)


/*
  [값이 없음 : undefined vs. null]
    - undefined는 변수 선언 시 값을 할당하지 않을 때 할당되는 값입니다.
    - null은 개발자가 의도적으로 값이 없음을 표현할 때 할당하는 값입니다.
*/

let unknown
console.log(unknown)

const nullValue = null 
console.log(nullValue)
console.log(typeof nullValue)  // object


/*
  [Boolean 타입 연습]

  자바스크립트의 Boolean 타입은 첫 단어가 소문자.
*/

let isLoggedIn = false
isLoggedIn = true

/*
  [삼항(Ternary) 연산자 연습]
  
  Tip. condition ? expression if true : expression if false
*/

const subscribed = false

if (subscribed === true) {
  console.log('구독중')
} else {
  console.log('구독취소')
}

const status = subscribed ? '구독중' : '구독취소'