// ES5 까지는 자바와 많이 유사하고 가독성이 나빴음
// 밑은 그 이후 버전
class Car {

  constructor({ title }) {
    this.title = title
  }
  /* 위와 같은 코드
  constructor(options) {
    this.title = options.title
  }
  */
 
  drive() {
    return 'Vroom'
  }
}

class Bmw extends Car {
  constructor(options) {
    super(options)
    this.color = options.color
  }

  honk() {
    return 'BBBMMWW'
  }

}

const car = new Car({ title: 'avante'})
const bmw = new Bmw({ title: '5 series', color: 'black'})

