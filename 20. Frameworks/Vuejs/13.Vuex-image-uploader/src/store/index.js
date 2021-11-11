import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import image from './modules/image'

Vue.use(Vuex)

// 기존 Store에 다 넣지 않고 module로 쪼갬
export default new Vuex.Store({
  modules: {
    auth, image,
  }
})
