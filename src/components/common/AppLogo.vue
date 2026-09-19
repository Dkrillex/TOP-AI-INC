<script setup>
import { brand } from '@/config/brand'

defineProps({
  compact: { type: Boolean, default: false },
})
</script>

<template>
  <div class="main-logo" :class="{ compact }">
    <svg class="mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <rect width="40" height="40" rx="10" fill="#2563EB" />
      <path d="M10 13h20v4H22v14h-4V17H10v-4Z" fill="#fff" />
      <circle cx="29" cy="28" r="4" fill="#93C5FD" />
    </svg>
    <span class="span-inter-800 main-logo-title">{{ brand.displayName }}</span>
  </div>
</template>

<style scoped>
.main-logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.mark {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
}

.main-logo-title {
  font-size: 20px;
  line-height: 20px;
  letter-spacing: -0.02em;
  color: var(--primary-text-color);
}

.compact .mark {
  width: 28px;
  height: 28px;
}

.compact .main-logo-title {
  font-size: 16px;
}
</style>
