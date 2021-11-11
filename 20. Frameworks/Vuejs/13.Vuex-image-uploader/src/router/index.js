import Vue from 'vue'
import VueRouter from 'vue-router'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
