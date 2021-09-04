import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AddComics from '../views/AddComics.vue'
import ReadComic from '../views/ReadComic.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
	{
		path: '/comics/add',
		name: 'AddComics',
		component: AddComics
	},
	{
		path: '/comics/:id/pages/:page',
		name: 'ReadComic',
		component: ReadComic
	}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
