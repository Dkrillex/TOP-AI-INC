<script setup>
import { computed } from 'vue'
import AppButton from '@/components/common/AppButton.vue'
import { useI18n } from '@/i18n'

const { t, messages } = useI18n()
const stats = computed(() => messages.value.home.stats)
</script>

<template>
  <section class="banner bg-grid">
    <div class="glow" />
    <div class="page-wrap banner-slot">
      <div class="hero-content">
        <div class="hero-text">
          <h1 class="span-inter-800 hero-title">
            {{ t('home.title') }}
          </h1>
          <p class="span-poppins-400 hero-desc">
            {{ t('home.desc') }}
          </p>
          <div class="hero-actions">
            <AppButton to="/contact" variant="primary" arrow>{{ t('common.book') }}</AppButton>
            <AppButton to="/products" variant="ghost">{{ t('common.explore') }}</AppButton>
          </div>
          <div class="trust">
            <article v-for="item in stats" :key="item.label" class="trust-item">
              <p class="span-inter-700 value">{{ item.value }}</p>
              <p class="span-inter-400 label">{{ item.label }}</p>
            </article>
          </div>
        </div>
        <div class="hero-visual">
          <img src="/images/hero-home.png" alt="Top AI enterprise platform" />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.banner {
  position: relative;
  overflow: hidden;
  background-color: #fff;
}

.glow {
  pointer-events: none;
  position: absolute;
  top: -120px;
  left: 12%;
  width: 420px;
  height: 420px;
  background: radial-gradient(circle, rgba(96, 165, 250, 0.28), transparent 68%);
}

.banner-slot {
  position: relative;
}

.hero-content {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 48px;
  align-items: center;
  min-height: 640px;
  padding: 48px 0 56px;
}

.hero-text {
  max-width: 560px;
}

.hero-title {
  margin: 0;
  font-size: 52px;
  line-height: 1.08;
  letter-spacing: -0.045em;
  color: var(--primary-text-color);
}

.hero-desc {
  margin: 20px 0 28px;
  max-width: 480px;
  color: var(--t-text-disable-color);
  font-size: 17px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.trust {
  display: flex;
  gap: 28px;
  margin-top: 36px;
  padding-top: 28px;
  border-top: 1px solid #f1f5f9;
}

.trust-item .value {
  margin: 0;
  font-size: 18px;
  letter-spacing: -0.03em;
}

.trust-item .label {
  margin: 4px 0 0;
  color: var(--t-text-disable-color);
  font-size: 12px;
}

.hero-visual {
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-visual img {
  display: block;
  width: 100%;
  height: auto;
  max-height: 520px;
  object-fit: contain;
  object-position: center;
}

@media (max-width: 960px) {
  .hero-content {
    grid-template-columns: 1fr;
    min-height: auto;
    padding: 40px 0 48px;
  }

  .hero-title {
    font-size: 36px;
  }

  .hero-visual img {
    max-height: 320px;
  }

  .trust {
    flex-wrap: wrap;
    gap: 16px 24px;
  }
}
</style>
