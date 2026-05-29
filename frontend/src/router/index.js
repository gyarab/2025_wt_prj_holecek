import { createRouter, createWebHistory } from 'vue-router'
import Kebabarna from '../views/kebablist.vue'
import KebabDetail from '../views/kebabdetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: Kebabarna },
        { path: '/kebab/:id', name: 'kebab-detail', component: KebabDetail },
    ]
})
export default router