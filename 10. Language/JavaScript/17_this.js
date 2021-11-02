/*
  브라우저의 모든 요소(Broser Object) === window 객체에 속해 있음

  중요 : this 키워드는 아래의 두 경우를 제외하고 모두 window
  1. 메서드에서 this === 객체 obj.method()
  2. constructor(생성자함수) 내부에서 this === class 가 생성한 객체(self 랑 같음)
*/
const user = {
  name: '강민구',
  greeting: function() {
    return `hello I am ${this.name}`
  }
}

user.greeting()

class Car {
  constructor({ title }) {
    this.title = title  // 2. 클래스 Car의 생성 객체
  }
}

const family = {
  status: 'happy',
  
  members: ['mom', 'dad', 'me', 'sister'],
  
  intro: function () {
    console.log('our family')
    this.members.forEach((member) => {  // 1. family.members
      console.log(`${this.status}: ${member}`)  // 1. family.status
    })
  }
}
family.intro()
