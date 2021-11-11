import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

import ImageList from '@/views/ImageList.vue'
import UploadForm from '@/views/UploadForm.vue'
import AuthHandler from '@/views/AuthHandler.vue'

Vue.use(VueRouter)

// name은 어디가서 쓰는거 아니니까 편하게 짓자
const routes = [
  {
    path: '/',
    name: 'Home',
    component: ImageList,
  },
  {
    path: '/upload',
    name: 'Upload',
    component: UploadForm
  },
  {
    path: '/oauth2/callback',
    name: 'AuthHandler',
    component: AuthHandler,
  },
  // {
  //   path: '/404',
  //   name: 'NotFound',
  //   component: NotFound,
  // },
  // {
  //   path: '*',
  //   redirect: '/404'
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

//page auth
router.beforeEach((to, from, next) => {
// 1. 로그인 해야만 함
  const authPages = ['Upload', ]
  const {isLoggedIn} = store.getters
  // 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)
  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요합니다. 로그인 후에 이용해주세요.')
    next('/')
  } else {
    next()
  }

// 2. 로그인 하면 안됨
// 3. 그 외
})

export default router
