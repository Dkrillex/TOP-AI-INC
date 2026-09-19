<script setup>
import AppHeader from './AppHeader.vue'
import AppFooter from './AppFooter.vue'
import AppHotline from './AppHotline.vue'
</script>

<template>
  <div class="main-layout">
    <AppHeader />
    <main>
      <router-view />
    </main>
    <AppFooter />
    <AppHotline />
  </div>
</template>

<style scoped>
.main-layout {
  min-height: 100vh;
  background: #fff;
}
</style>
