<script setup>
defineProps({
  name: { type: String, required: true },
})
</script>

<template>
  <svg class="icon" viewBox="0 0 48 48" fill="none" aria-hidden="true">
    <rect width="48" height="48" rx="12" fill="#EFF6FF" />
    <g v-if="name === 'routing'" stroke="#2563EB" stroke-width="2" stroke-linecap="round">
      <path d="M12 24h24" />
      <circle cx="24" cy="24" r="5" fill="#93C5FD" stroke="none" />
      <path d="M16 18c4-4 12-4 16 0M16 30c4 4 12 4 16 0" />
    </g>
    <g v-else-if="name === 'paths'" stroke="#2563EB" stroke-width="2" fill="none">
      <path d="M14 16c8 0 8 16 20 16" />
      <path d="M14 32c8 0 8-16 20-16" />
    </g>
    <g v-else-if="name === 'reliability'">
      <path d="M24 12c8 4 12 4 14 4v10c0 9-7 14-14 16-7-2-14-7-14-16V16c2 0 6 0 14-4Z" fill="#2563EB" />
      <path d="M20 24l3 3 6-7" stroke="#fff" stroke-width="2" stroke-linecap="round" />
    </g>
    <g v-else>
      <rect x="16" y="14" width="16" height="20" rx="3" fill="#2563EB" />
      <circle cx="24" cy="20" r="1.6" fill="#DBEAFE" />
      <circle cx="24" cy="25" r="1.6" fill="#DBEAFE" />
      <circle cx="24" cy="30" r="1.6" fill="#DBEAFE" />
    </g>
  </svg>
</template>

<style scoped>
.icon {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}
</style>
