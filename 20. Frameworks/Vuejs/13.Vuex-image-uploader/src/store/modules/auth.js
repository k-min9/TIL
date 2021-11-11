import imgurApi from '@/api/imgur'
import qs from 'qs'

import router from '@/router'  // 주소 조심
import cookies from 'vue-cookies'

const state = {
  // token: null,
  token : cookies.get('imgurToken'),  // 쿠키 버전
  //username : 'Guest',
  username: cookies.get('imgurUsername'),
}

const getters = {
  // 사용자가 로그인에게
  isLoggedIn: state => !!state.token  // 자바스크립트식 문법 표현 !! 표현을 true/false로 무조건 바꾸면서 3항 연산자의 행동을 함

}

const mutations = {
  SET_TOKEN(state, token) {
    state.token = token
  },
  SET_USERNAME(state, username) {
    state.username = username
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
    const userData = qs.parse(queryString)
    const token = qs.parse(queryString).access_token
    const username = userData.account_username

    commit('SET_TOKEN', token)  // state에 넣고
    commit('SET_USERNAME', username)

    // localStorage.setItem('imgurToken', token)  // 선택지 1 : local storage에 넣거나
    cookies.set('imgurToken', token)  // 선택지 2 : 쿠키에 넣거나
    cookies.set('imgurUsername', username)
    router.push('/')  // 홈으로 보내버리겠다.
  },

  logout({ commit }) {
    commit('SET_TOKEN', null)
    commit('SET_USERNAME', null)
    cookies.set('imgurToken', '')
    cookies.set('imgurUsername', '')

    //Refresh 해버리자
    window.location.path = '/'

  },

  // 액션에서 액션 호출(extract method 하고 싶을때) setCookies(_, obj) 같은 느낌으로 가능

}

export default {
  state, getters, mutations, actions,
}