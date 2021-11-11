import axios from 'axios'
import imgurApi from '@/api/imgur'

//Image module

const state = {
  images: [],
}

const getters = {
  // 모든 이미지를 받아오는 함수
  allImages(state) {
    return state.images
  }
}

const mutations = {
  SET_IMAGES: (state, images) => state.images = images
}

const actions = {
  // 1. 내가 업로드한 모든 이미지 받아오기
  fetchImages({ commit, rootState }) {
    // imgur 서식 authorization : Barer{{token}}
    const config = {
      headers: {
        'Authorization': `Bearer ${rootState.auth.token}`
      }
    }
    axios.get(imgurApi.IMAGE_URL, config)
      .then(res => commit('SET_IMAGES', res.data.data))    
  },
  // 2. 이미지 업로드하기



}

export default {
  state, getters, mutations, actions,
}