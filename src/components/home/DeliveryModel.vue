<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'

const { t, messages } = useI18n()
const deliverySteps = computed(() => messages.value.home.deliverySteps)

const icons = [
  'M12 12a4 4 0 1 0-4-4 4 4 0 0 0 4 4Zm-7 9a7 7 0 0 1 14 0',
  'M12 4v2m0 12v2m8-8h-2M6 12H4m12.5-4.5-1.4 1.4M7.9 16.1 6.5 17.5m10.6 0-1.4-1.4M7.9 7.9 6.5 6.5M12 8a4 4 0 1 1-4 4 4 4 0 0 1 4-4Z',
  'M8 4h8l2 4H6l2-4Zm-2 4h12v10a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8Zm4 4h4',
  'M12 7v5l3 2m6-2a9 9 0 1 1-3-6.7',
]
</script>

<template>
  <section class="global-delivery">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('home.deliveryEyebrow')"
        :title="t('home.deliveryTitle')"
      />
      <div class="gd-row">
        <article v-for="(item, index) in deliverySteps" :key="item.title" class="gd-card">
          <span class="span-inter-700 index">0{{ index + 1 }}</span>
          <svg class="gd-icon" viewBox="0 0 24 24" fill="none">
            <path :d="icons[index]" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <h3 class="span-inter-700 gd-card-title">{{ item.title }}</h3>
          <p class="span-poppins-400 gd-card-desc">{{ item.desc }}</p>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.global-delivery {
  padding: var(--section-y) 0;
  background: #fff;
}

.gd-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.gd-card {
  background: linear-gradient(180deg, #1d4ed8 0%, #0f172a 100%);
  border-radius: var(--radius-lg);
  padding: 28px 22px 32px;
  color: #fff;
  min-height: 268px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.gd-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 40px rgba(29, 78, 216, 0.28);
}

.index {
  display: block;
  margin-bottom: 18px;
  color: #93c5fd;
  font-size: 13px;
}

.gd-icon {
  width: 32px;
  height: 32px;
  margin-bottom: 16px;
  color: #dbeafe;
}

.gd-card-title {
  margin: 0 0 10px;
  font-size: 20px;
}

.gd-card-desc {
  margin: 0;
  color: rgba(255, 255, 255, 0.78);
  font-size: 14px;
  line-height: 1.7;
}

@media (max-width: 960px) {
  .gd-row {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .gd-row {
    grid-template-columns: 1fr;
  }
}
</style>
