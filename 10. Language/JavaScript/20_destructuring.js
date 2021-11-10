const context = {
  commit: function () {
    console.log('안녕하세요 commit!')
    return '여기 뭔가 더 써야되네'
  },
  state: {
    todo: '할 일 1',
  },
  getters: {},
  mutations: {},
}

// 1. 하나 하나 할당
// const commit = context.commit
// const state = context.state

// console.log(commit()) // 안녕하세요 commit!
// console.log(state) // { todo: '할 일 1' }

// Destructuring assignment
// 2. 이름으로 가져온다.
// 2.1 순서가 필요없고,
const { commit, state } = context
console.log(commit())
console.log(state)
console.log(state.todo)

// 2.2 한 개만 가져와도 상관없다.
// const { commit } = context
// console.log(commit())