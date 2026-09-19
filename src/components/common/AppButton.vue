<script setup>
defineProps({
  variant: { type: String, default: 'primary' },
  to: { type: String, default: '' },
  href: { type: String, default: '' },
  type: { type: String, default: 'button' },
  compact: { type: Boolean, default: false },
  arrow: { type: Boolean, default: false },
})
</script>

<template>
  <a
    v-if="href"
    :href="href"
    class="bubble-button"
    :class="[variant, { compact }]"
    target="_blank"
    rel="noopener noreferrer"
  >
    <span class="span-inter-600 label">
      <slot />
    </span>
    <span v-if="arrow" class="arrow" aria-hidden="true">→</span>
  </a>
  <router-link v-else-if="to" :to="to" class="bubble-button" :class="[variant, { compact }]" active-class="" exact-active-class="">
    <span class="span-inter-600 label">
      <slot />
    </span>
    <span v-if="arrow" class="arrow" aria-hidden="true">→</span>
  </router-link>
  <button v-else :type="type" class="bubble-button" :class="[variant, { compact }]">
    <span class="span-inter-600 label">
      <slot />
    </span>
    <span v-if="arrow" class="arrow" aria-hidden="true">→</span>
  </button>
</template>

<style scoped>
.bubble-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-width: 148px;
  height: 44px;
  padding: 0 22px;
  border-radius: 999px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: 0.2s ease;
  text-decoration: none;
  line-height: 1;
  vertical-align: middle;
}

.label {
  font-size: 14px;
  line-height: 1;
}

.arrow {
  font-size: 16px;
  line-height: 1;
  transform: translateY(-0.5px);
}

.primary {
  background: var(--primary-default-color);
  color: #fff;
  box-shadow: var(--btn-glow);
}

.primary:hover {
  background: var(--primary-hover-color);
  box-shadow: 0 12px 32px rgba(37, 99, 235, 0.4);
}

.ghost {
  background: #fff;
  color: var(--primary-text-color);
  border-color: #e2e8f0;
}

.ghost:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.light {
  background: #fff;
  color: var(--primary-text-color);
}

.light:hover {
  background: #f1f5f9;
}

.compact {
  min-width: 0;
  height: 36px;
  padding: 0 16px;
  box-shadow: none;
}

.compact .label {
  font-size: 13px;
  letter-spacing: 0.01em;
}
</style>
