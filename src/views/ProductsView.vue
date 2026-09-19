<script setup>
import { computed, ref, watch } from 'vue'
import { useI18n } from '@/i18n'
import AppButton from '@/components/common/AppButton.vue'
import FeatureIcon from '@/components/common/FeatureIcon.vue'
import VisionBanner from '@/components/home/VisionBanner.vue'

const { t, messages } = useI18n()
const icons = ['routing', 'paths', 'reliability', 'servers']
const products = computed(() => messages.value.products.items)
const active = ref(products.value[0].id)
const current = computed(() => products.value.find((item) => item.id === active.value) || products.value[0])

watch(products, (items) => {
  if (!items.some((item) => item.id === active.value)) {
    active.value = items[0].id
  }
})
</script>

<template>
  <section class="products-hero bg-grid">
    <div class="page-wrap hero-grid">
      <div class="copy">
        <p class="span-inter-500 kicker">{{ t('products.kicker') }}</p>
        <h1 class="span-inter-800 title">{{ t('products.title') }}</h1>
        <p class="span-poppins-400 lead">
          {{ t('products.lead') }}
        </p>
        <div class="actions">
          <AppButton to="/contact" variant="primary" arrow>{{ t('common.book') }}</AppButton>
          <AppButton to="/service" variant="ghost">{{ t('common.explore') }}</AppButton>
        </div>
      </div>
      <div class="visual">
        <img src="/images/products-hero.png" alt="Top AI modular platforms" />
      </div>
    </div>
  </section>

  <section class="products-body">
    <div class="tabs-bar">
      <div class="page-wrap tabs">
        <button
          v-for="item in products"
          :key="item.id"
          class="tab span-inter-600"
          :class="{ active: active === item.id }"
          type="button"
          @click="active = item.id"
        >
          {{ item.title }}
        </button>
      </div>
    </div>
    <div class="page-wrap detail">
      <div class="detail-copy">
        <p class="span-inter-700 eyebrow">{{ current.heading }}</p>
        <h2 class="span-inter-800 heading">{{ current.desc }}</h2>
        <div class="features">
          <article v-for="(feature, index) in current.features" :key="feature" class="feature">
            <FeatureIcon :name="icons[index] || 'servers'" />
            <p class="span-inter-600">{{ feature }}</p>
          </article>
        </div>
      </div>
      <div class="map-wrap">
        <img class="map" src="/images/world-map.png" alt="Top AI delivery map" />
      </div>
    </div>
  </section>

  <VisionBanner />
</template>

<style scoped>
.products-hero {
  position: relative;
  background-color: #fff;
}

.hero-grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 48px;
  align-items: center;
  min-height: 480px;
  padding: 72px 0;
}

.copy {
  max-width: 560px;
}

.visual {
  display: flex;
  align-items: center;
  justify-content: center;
}

.visual img {
  display: block;
  width: 100%;
  height: auto;
  max-height: 420px;
  object-fit: contain;
  object-position: center;
}

.kicker {
  display: inline-flex;
  margin: 0 0 16px;
  padding: 5px 12px;
  border: 1px solid #e2e8f0;
  border-radius: 999px;
  background: #fff;
  color: #475569;
  font-size: 12px;
}

.title {
  margin: 0 0 14px;
  max-width: 560px;
  font-size: 44px;
  line-height: 1.15;
  letter-spacing: -0.03em;
}

.lead {
  margin: 0 0 28px;
  max-width: 520px;
  color: var(--t-text-disable-color);
  font-size: 16px;
  line-height: 1.7;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.tabs-bar {
  background: #fff;
  border-bottom: 1px solid var(--line-subtle);
}

.tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 16px 0;
}

.tab {
  height: 40px;
  padding: 0 16px;
  border: 1px solid var(--line-subtle);
  border-radius: 999px;
  background: var(--surface);
  cursor: pointer;
  color: var(--t-text-disable-color);
  white-space: nowrap;
  transition: 0.2s ease;
}

.tab:hover {
  color: var(--primary-default-color);
  border-color: #bfdbfe;
  background: #fff;
}

.tab.active {
  color: #fff;
  background: var(--primary-default-color);
  border-color: var(--primary-default-color);
}

.detail {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 48px;
  align-items: center;
  padding: 64px 0 var(--section-y);
}

.eyebrow {
  display: inline-flex;
  margin: 0 0 12px;
  padding: 5px 12px;
  border: 1px solid #e2e8f0;
  border-radius: 999px;
  background: #fff;
  color: #475569;
  font-size: 12px;
  letter-spacing: 0;
  text-transform: none;
}

.heading {
  margin: 0 0 28px;
  font-size: 22px;
  line-height: 1.5;
}

.features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.feature {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 16px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.feature p {
  margin: 0;
  font-size: 14px;
  line-height: 1.45;
}

.map-wrap {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-xl);
  padding: 20px;
}

.map {
  width: 100%;
  border-radius: var(--radius-md);
  display: block;
}

@media (max-width: 960px) {
  .hero-grid,
  .detail,
  .features {
    grid-template-columns: 1fr;
  }

  .hero-grid {
    min-height: auto;
    padding: 48px 0 40px;
  }

  .title {
    font-size: 34px;
  }

  .visual img {
    max-height: 280px;
  }
}
</style>
