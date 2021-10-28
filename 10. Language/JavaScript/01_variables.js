/*
  [let 키워드 연습]
  let => 변수 / 특징 : 재할당
*/
let location
location = '제주도'
location = '서울'

/*
  [const 키워드 연습]  
  const => 상수 / 특징 : 재할당 불가능 error
*/
const phone = 'Galaxy S2'
phone = 'zflip'

/*
  [var 키워드 연습]  
  let => 변수 / 특징 : 재선언, 재할당.
*/

var framework = 'Bootstrap'
framework = 'Django'
var framework = 'Vue'

//===============================================

/*
  [블록 스코프 - let]
  변수의 생명주기가 중괄호 내부
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName)
}
console.log('전역 스코프:', fullName)

/*
  [블록 스코프 - const 예시]  
  상수의 생명주기가 중괄호 내부
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  const language = 'Python'
}
console.log(language)

/*
  [함수 스코프 - var 키워드 예시]
  
*/

function f1() {
  var message = 'You are doing great!'
}
f1()
console.log(message)


/*
  [블록 스코프 - var, const, let 키워드 예시]
  Tip. if문은 블록 스코프를 생성합니다.
*/

//var
const codeEditor = 'vscode'
if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)

//const
function f2() {
  const stack = 'Last In, First Out'
}
f2()
console.log(stack)

//let
function f3() {
  let queue = 'First In, First Out'
}
f3()
console.log(queue)


/*
  [호이스팅(hoisting)]  : 선언과 할당을 분리하여 유효범위의 최상단으로 올리는 행위 
  (일단은 var 특징으로)
  그리고 const와 let의 경우와 비교해보세요.
*/

console.log(hoisted)
var hoisted = 'can you see me?'  // undefined

console.log(lunch)
const lunch = '초밥'  // error

console.log(dinner)
let dinner = '스테이크'  // error