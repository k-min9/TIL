const data = [
  {id: 1, content: 'hi', completed: true},
  {id: 2, content: 'gi', completed: true},
  {id: 3, content: 'di', completed: true},
  {id: 4, content: 'qi', completed: true},
]

// json 보낼 때는 단순한 string 덩어리
const jsonString = JSON.stringify(data)

// 받은 json을 Object로 바꿔서(파싱) 사용
const recoveredData = JSON.parse(jsonString)