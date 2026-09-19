<script setup>
import { computed, ref } from 'vue'
import { brand } from '@/config/brand'
import { useI18n } from '@/i18n'
import AppLogo from '@/components/common/AppLogo.vue'
import AppButton from '@/components/common/AppButton.vue'

const { t, messages } = useI18n()
const email = ref('')
const subscribed = ref(false)

const footerFeatures = computed(() => [
  { label: messages.value.nav.home, path: '/' },
  { label: messages.value.nav.aboutUs, path: '/about' },
  { label: messages.value.nav.products, path: '/products' },
  { label: messages.value.nav.services, path: '/service' },
  { label: messages.value.nav.network, path: '/global-network' },
  { label: messages.value.nav.contactUs, path: '/contact' },
])

function subscribe() {
  if (!email.value.includes('@')) return
  subscribed.value = true
  email.value = ''
}
</script>

<template>
  <footer class="site-footer">
    <div class="contact-content">
      <div class="page-wrap grid">
        <div class="contact-content-left">
          <div class="contact-content-search">
            <h3 class="span-inter-700 contact-content-search-title">{{ t('common.stayUpdated') }}</h3>
            <p class="span-inter-400 contact-content-search-desc">
              {{ t('common.stayDesc') }}
            </p>
            <form class="email-input-wrapper" @submit.prevent="subscribe">
              <input
                v-model="email"
                class="email-input"
                type="email"
                :placeholder="t('common.emailPlaceholder')"
                required
              />
              <AppButton type="submit" variant="primary">{{ subscribed ? t('common.subscribed') : t('common.subscribe') }}</AppButton>
            </form>
          </div>
          <div class="contact-content-info">
            <p class="span-inter-600 info-title">{{ t('common.contactUs') }}</p>
            <a class="contact-content-info-item" :href="brand.emailHref">{{ brand.email }}</a>
            <p class="contact-content-info-item address">{{ brand.address }}</p>
          </div>
        </div>
        <div class="contact-content-right">
          <div class="contact-content-feature">
            <p class="span-inter-600 contact-content-feature-title">{{ t('common.exploreTitle') }}</p>
            <div class="contact-content-feature-content">
              <router-link v-for="item in footerFeatures" :key="item.label" class="span-inter-400 link" :to="item.path">
                {{ item.label }}
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="main-footer">
      <div class="page-wrap bar">
        <p class="span-inter-400 main-footer-rights">{{ brand.copyright }}</p>
        <AppLogo compact />
      </div>
    </div>
  </footer>
</template>

<style scoped>
.contact-content {
  background: #fff;
  padding: 64px 0 48px;
  border-top: 1px solid #f1f5f9;
}

.grid {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr;
  gap: 48px;
}

.contact-content-search-title {
  margin: 0 0 8px;
  font-size: 22px;
}

.contact-content-search-desc {
  margin: 0 0 18px;
  color: var(--t-text-disable-color);
}

.email-input-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
  max-width: 520px;
}

.email-input {
  flex: 1;
  height: 44px;
  border: 1px solid var(--grey-color);
  border-radius: 999px;
  padding: 0 18px;
  outline: none;
  background: #fff;
}

.email-input:focus {
  border-color: var(--primary-default-color);
}

.contact-content-info {
  margin-top: 32px;
}

.info-title {
  margin: 0 0 10px;
}

.contact-content-info-item {
  display: block;
  margin-bottom: 8px;
  color: var(--t-text-disable-color);
}

.contact-content-feature-title {
  margin: 0 0 14px;
}

.contact-content-feature-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px 24px;
}

.link {
  color: var(--t-text-disable-color);
}

.link:hover {
  color: var(--primary-default-color);
}

.main-footer {
  background: #fff;
  border-top: 1px solid #eef2f7;
}

.bar {
  min-height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.main-footer-rights {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
}

@media (max-width: 860px) {
  .grid,
  .email-input-wrapper,
  .bar {
    display: block;
  }

  .contact-content-right,
  .bar :deep(.main-logo) {
    margin-top: 28px;
  }
}
</style>
