const todoItem = {
  todo: '첫 번째 할 일',
  dueDate: '1999-12-12',
  importance: 'high',
  isCompleted: false,
}

// isCompleted 값만 변경한다고 가정
// 1. 첫 번째 방법
const myUpdateTodo = {
  todo: '첫 번째 할 일',
  duteDate: '1999-12-12',
  importance: 'high',
  isCompleted: true,
}

console.log(myUpdateTodo)

// 2. 두 번째 방법
const myUpdateTodo2 = {
  ...todoItem,
  isCompleted: true,
}

console.log('---')
console.log(myUpdateTodo2)