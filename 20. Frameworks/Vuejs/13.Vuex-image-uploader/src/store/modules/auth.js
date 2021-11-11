import imgurApi from '@/api/imgur'
import qs from 'qs'

import router from 'vue-router'
import cookies from 'vue-cookies'

const state = {
  // token: null,
  token : cookies.get('imgurToken'),  // 쿠키 버전
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
  // 사용자를 imgur 로그인 창으로 보냄
  login() {
    // const fullUrl = '${imgurApi.ROOT_URL}/oauth2/...' 이 방식은 너무 길고 지저분
    // 이왕 긁어올거 그냥 api>imgur.js에서 완성 상태로 긁어오자
    imgurApi.login()
  },
  // 받은 토큰으로 state 세팅
  finalizeLogin({ commit }, queryString) {
    const token = qs.parse(queryString).access_token
    commit('SET_TOKEN', token)  // state에 넣고
    // localStorage.setItem('imgurToken', token)  // 선택지 1 : local storage에 넣거나
    cookies.set('imgurToken', token)  // 선택지 2 : 쿠키에 넣거나
    router.push('/')  // 홈으로 보내버리겠다.
  },
  logout({ commit }) {
    commit('SET_TOKEN', null)
    cookies.set('imgurToken', '')
  }
}

export default {
  state, getters, mutations, actions,
}