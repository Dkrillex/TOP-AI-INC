<script setup>
import { computed, ref } from 'vue'
import { useI18n } from '@/i18n'
import AppLogo from '@/components/common/AppLogo.vue'

const { t, messages } = useI18n()
const open = ref(false)

const navItems = computed(() => [
  { label: messages.value.nav.home, path: '/' },
  { label: messages.value.nav.about, path: '/about' },
  { label: messages.value.nav.products, path: '/products' },
  { label: messages.value.nav.service, path: '/service' },
  { label: messages.value.nav.network, path: '/global-network' },
  { label: messages.value.nav.contact, path: '/contact' },
])
</script>

<template>
  <header class="main-header">
    <div class="page-wrap inner">
      <router-link to="/" class="logo-link" @click="open = false">
        <AppLogo />
      </router-link>
      <button class="menu-toggle" type="button" :aria-label="t('common.toggleMenu')" @click="open = !open">
        <span />
        <span />
      </button>
      <div class="header-right" :class="{ open }">
        <nav class="header-tab">
          <router-link
            v-for="item in navItems"
            :key="item.path"
            :to="item.path"
            class="header-tab-button"
            @click="open = false"
          >
            <span class="span-inter-500 header-tab-button-title">{{ item.label }}</span>
          </router-link>
        </nav>
      </div>
    </div>
  </header>
</template>

<style scoped>
.main-header {
  position: sticky;
  top: 0;
  z-index: 20;
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid #f1f5f9;
}

.inner {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.logo-link {
  display: flex;
  align-items: center;
  flex-shrink: 0;
  height: 36px;
}

.header-right {
  display: flex;
  align-items: center;
  height: 36px;
  gap: 8px;
}

.header-tab {
  display: flex;
  align-items: center;
  height: 36px;
  gap: 2px;
}

.header-tab-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 36px;
  padding: 0 12px;
  line-height: 1;
  color: #64748b;
}

.header-tab-button-title {
  font-size: 14px;
  line-height: 1;
}

.header-tab-button:hover,
.header-tab-button.router-link-exact-active {
  color: var(--primary-text-color);
}

.menu-toggle {
  display: none;
  width: 40px;
  height: 40px;
  border: 0;
  background: transparent;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
}

.menu-toggle span {
  display: block;
  height: 1.5px;
  background: var(--primary-text-color);
}

@media (max-width: 1080px) {
  .header-tab-button {
    padding: 0 8px;
  }
}

@media (max-width: 960px) {
  .menu-toggle {
    display: flex;
  }

  .header-right {
    display: none;
    position: absolute;
    top: var(--header-height);
    left: 0;
    right: 0;
    height: auto;
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
    padding: 16px 24px 20px;
    background: #fff;
    border-bottom: 1px solid #f1f5f9;
  }

  .header-right.open {
    display: flex;
  }

  .header-tab {
    height: auto;
    flex-direction: column;
    align-items: stretch;
  }

  .header-tab-button {
    height: 42px;
  }
}
</style>
