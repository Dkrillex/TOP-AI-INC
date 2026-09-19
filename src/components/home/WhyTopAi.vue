<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'
import AppButton from '@/components/common/AppButton.vue'

const { t, messages } = useI18n()
const whyCards = computed(() => messages.value.home.whyCards)
</script>

<template>
  <section class="global-licensed">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('home.whyEyebrow')"
        :title="t('home.whyTitle')"
        :desc="t('home.whyDesc')"
      />
      <div class="gl-grid">
        <article v-for="item in whyCards" :key="item.title" class="gl-card">
          <div>
            <h3 class="span-inter-700 gl-card-title">{{ item.title }}</h3>
            <p class="span-poppins-400 gl-card-desc">{{ item.desc }}</p>
          </div>
          <AppButton to="/about" variant="ghost">{{ t('common.knowMore') }}</AppButton>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.global-licensed {
  padding: 64px 0 var(--section-y);
  background: #fff;
}

.gl-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.gl-card {
  background: #fff;
  border-radius: var(--radius-lg);
  padding: 28px 26px;
  border: 1px solid #e2e8f0;
  min-height: 216px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.gl-card:hover {
  transform: translateY(-3px);
  border-color: #cbd5e1;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.06);
}

.gl-card-title {
  margin: 0 0 10px;
  font-size: 20px;
  line-height: 1.4;
}

.gl-card-desc {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 14px;
  line-height: 1.7;
}

@media (max-width: 768px) {
  .gl-grid {
    grid-template-columns: 1fr;
  }
}
</style>
