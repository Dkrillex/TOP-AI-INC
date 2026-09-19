<script setup>
import { ref } from 'vue'
import { brand } from '@/config/brand'
import { useI18n } from '@/i18n'

const { t } = useI18n()
const active = ref('')
</script>

<template>
  <aside class="global-hotline">
    <div class="hotline-frame">
      <div
        class="hotline-item-wrap"
        @mouseenter="active = 'email'"
        @mouseleave="active = ''"
      >
        <div class="hotline-item">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none">
            <rect x="3" y="5" width="18" height="14" rx="2" stroke="#fff" stroke-width="1.6" />
            <path d="m4 7 8 6 8-6" stroke="#fff" stroke-width="1.6" />
          </svg>
          <span class="span-inter-600 hotline-text">{{ t('common.email') }}</span>
        </div>
        <div v-if="active === 'email'" class="hotline-tooltip">
          <div class="hotline-tooltip-head">
            <span class="span-inter-700">{{ t('common.email') }}</span>
          </div>
          <a class="hotline-number span-inter-500" :href="brand.emailHref">{{ brand.email }}</a>
          <p class="hotline-time span-poppins-400">{{ t('common.response') }}: {{ brand.response }}</p>
        </div>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.global-hotline {
  position: fixed;
  right: 0;
  top: 42%;
  z-index: 30;
}

.hotline-frame {
  width: 56px;
  overflow: visible;
  border-radius: 16px 0 0 16px;
  background: var(--hotline-color);
  box-shadow: -4px 8px 20px rgba(37, 99, 235, 0.28);
}

.hotline-item-wrap {
  position: relative;
}

.hotline-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  min-height: 78px;
  color: #fff;
  cursor: pointer;
}

.hotline-text {
  font-size: 11px;
  writing-mode: horizontal-tb;
}

.hotline-tooltip {
  position: absolute;
  right: 68px;
  top: 50%;
  transform: translateY(-50%);
  width: 220px;
  padding: 14px 16px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(15, 40, 80, 0.12);
}

.hotline-tooltip-head {
  margin-bottom: 8px;
  color: var(--primary-text-color);
}

.hotline-number {
  display: block;
  color: var(--primary-default-color);
  font-size: 15px;
}

.hotline-time {
  margin: 6px 0 0;
  color: var(--t-text-disable-color);
  font-size: 12px;
}

@media (max-width: 768px) {
  .global-hotline {
    display: none;
  }
}
</style>
