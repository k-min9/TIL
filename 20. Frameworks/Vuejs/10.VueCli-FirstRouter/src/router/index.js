import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import TheLunch from '@/views/TheLunch.vue'  // @도 같은식
import TheLotto from '../views/TheLotto.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',  // named routes >> route-link나, 프로그래밍 방식 네비게이션($router.push)등에 사용
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/lunch',
    name: 'TheLunch',
    component: TheLunch
  },
  {
    path: '/lotto/:lottoNum',
    name: 'TheLotto',
    component: TheLotto,
  },
  {
    // 이렇게 해야 페이지에 404가 표시가 됨
    path: '/404',
    name: 'NotFound',
    component: NotFound,
  },
  // 위에서 쭉 긁어오면서 없음 = 404 에러 -> 보내기
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
