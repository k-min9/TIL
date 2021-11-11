import axios from 'axios'
import imgurApi from '@/api/imgur'
import router from '@/router'

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
  fetchImages({ commit, rootState, rootGetters }) {
    // 로그인 되어 있을 때만 기본 값 긁어오겠다.
    if (rootGetters.isLoggedIn) {
    // imgur 서식 authorization : Barer{{token}}
    const { token } = rootState.auth
    const config = {
      headers: { 
        'Authorization': `Bearer ${token}`, 
      },
    }
    axios.get(imgurApi.IMAGES_URL, config)
      .then(res => commit('SET_IMAGES', res.data.data))    
      .catch(err => console.error(err))
    }
  },
  // 2. 이미지 (여러장) 업로드하기
  uploadImages({ rootState }, event) {
    // console.log(context)
    // console.log(event)
    const token = rootState.auth.token
    const images = Array.from(event.target.files)

    const config = {
      headers: {
        'Authorization': `Bearer ${token}`
      },
    }
    
    const promises = []

    images.forEach(image => {
      const formData = new FormData()
      formData.append('image', image)

      // // 비동기
      // axios.post(imgurApi.UPLOAD_URL, formData, config)
      // .then(res => console.log(res.data))
      // .catch(err => console.error(err))

      // // 동기 -> 순서 꼬임 : Promise.all() 사용하자
      // router.push({ name:'Home' })

      const p = axios.post(imgurApi.UPLOAD_URL, formData, config)
      promises.push(p)
    })

    Promise.all(promises)
    .then(() => router.push({ name: 'Home' }))
    .catch(err => console.error(err))

  }


}

export default {
  state, getters, mutations, actions,
}