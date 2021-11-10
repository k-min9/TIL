import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const URL = 'https://jsonplaceholder.typicode.com/users/1/todos'

export default new Vuex.Store({
  state: {
    todos: []
  },
  getters:{

  },
  mutations: {
    // 비동기 동작 절대 넣지마라! (dev 툴에서 추적을 못함)
    UPDATE_TODOS(state, todos) {
      state.todos = todos
    },
    UPDATE_TODO(state, newTodo) {
      const oldTodo = state.todos.find(todo => todo.id === newTodo.id)

      for (const key in oldTodo) {
        oldTodo[key] = newTodo[key]
      }
    }
  },
  actions: {
    // context는 도구 모음이라고 생각하면 편하다. 단지 commit만 쓸꺼니까 { commit }으로
    async fetchTodos({ commit }) {
      const res = await fetch(URL)
      const todos = await res.json()
      commit('UPDATE_TODOS', todos)  // todos를 mutation UPDATE_TODOS에 인자로
    },
    updateTodo({ commit }, newTodo) {
      commit('UPDATE_TODO', newTodo)
      // 앞으로 할 일, 서버 DB 내용도 변동
      // axios.post(SERVER_URL, newTodo)
      // axios.put('domain.com/todos/1', newTodo)
    }
  },
  //modules: {}
})
