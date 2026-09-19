<script setup>
defineProps({
  name: { type: String, required: true },
})
</script>

<template>
  <svg class="icon" viewBox="0 0 56 56" fill="none" aria-hidden="true">
    <rect width="56" height="56" rx="16" fill="#EFF6FF" />
    <g v-if="name === 'email'">
      <rect x="12" y="16" width="32" height="24" rx="4" fill="#2563EB" />
      <path d="m14 20 14 10 14-10" stroke="#fff" stroke-width="2.2" />
    </g>
    <g v-else-if="name === 'clock'">
      <circle cx="28" cy="28" r="14" fill="#2563EB" />
      <path d="M28 20v9l6 4" stroke="#fff" stroke-width="2.2" stroke-linecap="round" />
    </g>
    <g v-else-if="name === 'phone'">
      <path d="M20 16h8l3 8-5 3a18 18 0 0 0 9 9l3-5 8 3v8a4 4 0 0 1-4 4C27 46 16 35 16 20a4 4 0 0 1 4-4Z" fill="#2563EB" />
    </g>
    <g v-else>
      <path d="M28 14c7 0 13 6 13 14 0 10-13 20-13 20S15 38 15 28c0-8 6-14 13-14Z" fill="#2563EB" />
      <circle cx="28" cy="27" r="5" fill="#DBEAFE" />
    </g>
  </svg>
</template>

<style scoped>
.icon {
  width: 56px;
  height: 56px;
}
</style>
