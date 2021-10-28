/*
[Object 축약 문법]

아래 변수들을 속성으로 가지는 Object를 축약문법을 활용하여 작성하세요.
*/

const username = 'hailey'
const contact = '010-1234-5678'

const user1 = {
  username: username,
  contact: contact,
}

const user2 = {
  username,
  contact,
}

console.log(user1)
console.log(user2)

/*
[Object Destructuring] : 구조 분해할당

주어진 함수를 Object 축약 문법과, destructuring을 사용하여 재작성하세요.
*/

const users = [
  {
    name: 'hailey',
    contact: '010-1234-5678',
  },
  {
    name: 'paul',
    contact: '010-5678-1234',
  },
]


const userData1 = users.map((user, index) => {
    return { id: index, name: user.name, contact: user.contact }
})

const userData2 = users.map(function({ name, contact }, idx) {
  return { id: idx, name, contact }
})

console.log(userData1)
console.log(userData2)