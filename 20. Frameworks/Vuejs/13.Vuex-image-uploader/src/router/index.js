import Vue from 'vue'
import VueRouter from 'vue-router'

import AuthHandler from '@/views/AuthHandler.vue'

Vue.use(VueRouter)

const routes = [
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
