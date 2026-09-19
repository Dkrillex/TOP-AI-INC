<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import DeliveryModel from '@/components/home/DeliveryModel.vue'
import VisionBanner from '@/components/home/VisionBanner.vue'
import SectionHeader from '@/components/common/SectionHeader.vue'
import AppButton from '@/components/common/AppButton.vue'

const { t, messages } = useI18n()
const slas = computed(() => messages.value.service.slas)
const offerings = computed(() => messages.value.service.offerings)
</script>

<template>
  <section class="service-hero bg-grid">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('service.eyebrow')"
        :title="t('service.title')"
        :desc="t('service.desc')"
      />
      <div class="actions">
        <AppButton to="/contact" variant="primary" arrow>{{ t('common.book') }}</AppButton>
        <AppButton to="/products" variant="ghost">{{ t('common.explore') }}</AppButton>
      </div>
      <div class="sla-grid">
        <article v-for="item in slas" :key="item.label" class="sla">
          <p class="span-inter-800 value">{{ item.value }}</p>
          <p class="span-poppins-400 label">{{ item.label }}</p>
        </article>
      </div>
    </div>
  </section>

  <section class="offerings">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('service.offeringsEyebrow')"
        :title="t('service.offeringsTitle')"
        :desc="t('service.offeringsDesc')"
      />
      <div class="offer-grid">
        <article v-for="(item, index) in offerings" :key="item.title" class="offer">
          <span class="span-inter-700 index">0{{ index + 1 }}</span>
          <h3 class="span-inter-700">{{ item.title }}</h3>
          <p class="span-poppins-400">{{ item.desc }}</p>
        </article>
      </div>
    </div>
  </section>

  <DeliveryModel />
  <VisionBanner />
</template>

<style scoped>
.service-hero {
  padding: var(--section-y) 0 40px;
  background-color: #fff;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin: -8px 0 36px;
}

.sla-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.sla {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  padding: 28px 18px;
  text-align: center;
}

.value {
  margin: 0;
  font-size: 32px;
  letter-spacing: -0.03em;
  color: var(--primary-text-color);
}

.label {
  margin: 8px 0 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
}

.offerings {
  padding: 40px 0 24px;
  background: #fff;
}

.offer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.offer {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  padding: 28px 22px;
  min-height: 220px;
}

.index {
  display: block;
  margin-bottom: 18px;
  color: var(--primary-default-color);
  font-size: 13px;
  letter-spacing: 0.08em;
}

.offer h3 {
  margin: 0 0 10px;
  font-size: 18px;
}

.offer p {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 14px;
  line-height: 1.7;
}

@media (max-width: 960px) {
  .sla-grid,
  .offer-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .sla-grid,
  .offer-grid {
    grid-template-columns: 1fr;
  }
}
</style>
