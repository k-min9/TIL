import imgurApi from '@/api/imgur'

const stat = {
  token: null,
}

const getters = {
  // 사용자가 로그인에게
  isLoggedIn: state => state.token  // 자바스크립트식 문법 표현 !! 표현을 true/false로 무조건 바꾸면서 3항 연산자의 행동을 함

}

const mutations = {
  SET_TOKEN(state, token) {
    state.token = token
  }
}

const actions = {
  login() {
    // const fullUrl = '${imgurApi.ROOT_URL}/oauth2/...' 이 방식은 너무 길고 지저분
    // 이왕 긁어올거 그냥 api>imgur.js에서 완성 상태로 긁어오자
    imgurApi.login()
  },
  logout({ commit }) {
    commit('SET_TOKEN', null)
  }
}

export default {
  state, getters, mutations, actions,
}