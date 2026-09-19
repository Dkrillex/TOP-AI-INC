<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'
import VisionBanner from '@/components/home/VisionBanner.vue'
import AppButton from '@/components/common/AppButton.vue'

const { t, messages } = useI18n()
const stats = computed(() => messages.value.network.stats)
const points = computed(() => messages.value.network.points)
</script>

<template>
  <section class="network bg-grid">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('network.eyebrow')"
        :title="t('network.title')"
        :desc="t('network.desc')"
      />
      <div class="actions">
        <AppButton to="/contact" variant="primary" arrow>{{ t('common.book') }}</AppButton>
        <AppButton to="/products" variant="ghost">{{ t('common.explore') }}</AppButton>
      </div>
      <div class="map-wrap">
        <img class="map" src="/images/world-map.png" alt="Top AI Texas presence" />
        <div class="chips">
          <article v-for="item in stats" :key="item.label" class="chip">
            <p class="span-inter-800 value">{{ item.value }}</p>
            <p class="span-poppins-400 label">{{ item.label }}</p>
          </article>
        </div>
      </div>
      <div class="cards">
        <article v-for="(item, index) in points" :key="item.title" class="card">
          <span class="span-inter-700 index">0{{ index + 1 }}</span>
          <h3 class="span-inter-700">{{ item.title }}</h3>
          <p class="span-poppins-400">{{ item.desc }}</p>
        </article>
      </div>
    </div>
  </section>
  <VisionBanner />
</template>

<style scoped>
.network {
  padding: var(--section-y) 0 40px;
  background-color: #fff;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin: -8px 0 36px;
}

.map-wrap {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-xl);
  padding: 24px 24px 20px;
  margin-bottom: 28px;
}

.map {
  width: 100%;
  display: block;
  border-radius: var(--radius-md);
}

.chips {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 20px;
}

.chip {
  background: #fff;
  border: 1px solid var(--line-subtle);
  border-radius: 14px;
  padding: 16px 12px;
  text-align: center;
}

.value {
  margin: 0;
  font-size: 22px;
  color: var(--primary-text-color);
}

.label {
  margin: 4px 0 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
}

.cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.card {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  padding: 24px 20px 26px;
}

.index {
  display: block;
  margin-bottom: 14px;
  color: var(--primary-default-color);
  font-size: 13px;
  letter-spacing: 0.08em;
}

.card h3 {
  margin: 0 0 8px;
  font-size: 16px;
}

.card p {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
  line-height: 1.7;
}

@media (max-width: 860px) {
  .cards,
  .chips {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 560px) {
  .cards,
  .chips {
    grid-template-columns: 1fr;
  }
}
</style>
