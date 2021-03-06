import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

const Home = () => import('../views/Home.vue')
const ReadComic = () => import('../views/ReadComic.vue')

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/readers/comic-reader/:id',
    name: 'ReadComic',
    component: ReadComic
  },
  {
    path: '*',
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
