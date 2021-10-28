// array helper methods

/*
 [배열 관련 주요 메서드 연습 심화 1]
 
 속력(distance/time)을 저장하는 배열 speeds를 만드세요.
*/

const trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 },
]

const results = []
for (const obj of trips) {
  results.push(obj.distance / obj.time)
}

trips.map(function(trip) {
  return trip.distance / trip.time
})

trips.map(trip => trip.distance / trip.time)

/*
 [배열 관련 주요 메서드 연습 심화 2] : filter
 
 주어진 배열의 요소 중 특정 문자(query)가 포함되는 요소만 모아서 새로운 배열을 반환하세요.
*/

const languages = ['python', 'javascript', 'html', 'java']
const query = 'java'

languages.filter(function(language) {
  return language.includes(query)
})

languages.filter(language => language.includes(query))

/*
 [배열 관련 주요 메서드 연습 심화 3] : reduce => 쌓아 나간다.
 
 주어진 배열을 사용하여 다음과 같은 객체를 만드세요.
 {
   smith: 90,
   peter: 80,
   anna: 85,
 }
*/

const numbers= [1, 2, 3, 4]

// [1,2,3,4]와 같은 표현
numbers.reduce(function(acc, number) { // .reduce(func, acc) 
  return acc * number
}, 1) // (acc === 쌓아나갈 바닥)
console.log(numbers)


const students = [
  { name: 'smith', score: 90 },
  { name: 'peter', score: 80 },
  { name: 'anna', score: 85 },
]
const scoreObj = students.reduce(function(acc, student) {
  acc[student.name] = student.score
  return acc
}, {}) // (acc === 쌓아나갈 바닥)
console.log(scoreObj)


/*
 [배열 관련 주요 메서드 연습 심화 4] : find

 주어진 accounts 배열에서 balance가 24,000인 사람을 찾으세요.
*/

const accounts = [
	{ name: 'justin', balance: 1200 },
	{ name: 'harry', balance: 50000 },
	{ name: 'jason', balance: 24000 },
	{ name: 'neo', balance: 24000 },
]

accounts.find(function(account) {
  if (account.balance === 24000) {
    return account
  }
})


/*
 [배열 관련 주요 메서드 연습 심화 5] : some = return 중 하나라도 true시 true
 
 주어진 requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
*/

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

requests.some(function(request) {
  return request.status === 'pending'
})

/*
 [배열 관련 주요 메서드 연습 심화 6] : every = return 전부 true 시 true
 
 주어진 users 배열을 통해 모든 유저의 상태가 submmited인지 여부를 확인하세요.
*/

const users = [
  {name: 'neo', submitted: true},
  {name: 'eric', submitted: false},
  {name: 'tony', submitted: true},
]

users.every(function(user) {
  return user.submitted
})


/* 
 [배열 관련 주요 메서드 연습 심화 7] : forEach : 반환이 없고 각각의 요소에 대해 주어진 함수를 시행
 */

const numbers = [1, 2, 3]

numbers.forEach(function(number) {
  console.log(number)
})

