import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior() {
    return { top: 0 }
  },
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/about', name: 'about', component: () => import('@/views/AboutView.vue') },
    { path: '/products', name: 'products', component: () => import('@/views/ProductsView.vue') },
    { path: '/service', name: 'service', component: () => import('@/views/ServiceView.vue') },
    { path: '/global-network', name: 'global-network', component: () => import('@/views/GlobalNetworkView.vue') },
    { path: '/contact', name: 'contact', component: () => import('@/views/ContactView.vue') },
  ],
})

export default router
