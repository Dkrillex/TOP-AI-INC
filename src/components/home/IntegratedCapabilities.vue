<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'
import CapabilityIcon from '@/components/common/CapabilityIcon.vue'

const { t, messages } = useI18n()
const capabilities = computed(() => messages.value.home.capabilities)
</script>

<template>
  <section class="global-integrated">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('home.capabilitiesEyebrow')"
        :title="t('home.capabilitiesTitle')"
        :desc="t('home.capabilitiesDesc')"
      />
      <div class="gi-grid">
        <article v-for="item in capabilities" :key="item.title" class="gi-card">
          <CapabilityIcon :name="item.icon" />
          <div>
            <h3 class="span-inter-700 gi-card-title">{{ item.title }}</h3>
            <p class="span-poppins-400 gi-card-desc">{{ item.desc }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.global-integrated {
  padding: var(--section-y) 0 64px;
  background: #fff;
}

.gi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.gi-card {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  min-height: 148px;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.gi-card:hover {
  transform: translateY(-3px);
  border-color: #cbd5e1;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.06);
}

.gi-card-title {
  margin: 0 0 8px;
  font-size: 18px;
}

.gi-card-desc {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 14px;
  line-height: 1.7;
}

@media (max-width: 768px) {
  .gi-grid {
    grid-template-columns: 1fr;
  }
}
</style>
