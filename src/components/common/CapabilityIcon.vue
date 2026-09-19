<script setup>
const props = defineProps({
  name: { type: String, required: true },
})
const blueId = `cap-blue-${props.name}`
const mintId = `cap-mint-${props.name}`
</script>

<template>
  <svg class="icon" viewBox="0 0 88 88" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <defs>
      <linearGradient :id="blueId" x1="12" y1="8" x2="70" y2="72">
        <stop offset="0%" stop-color="#93C5FD" />
        <stop offset="100%" stop-color="#2563EB" />
      </linearGradient>
      <linearGradient :id="mintId" x1="40" y1="30" x2="86" y2="86">
        <stop offset="0%" stop-color="#DBEAFE" />
        <stop offset="100%" stop-color="#60A5FA" />
      </linearGradient>
    </defs>

    <g v-if="name === 'network'">
      <circle cx="58" cy="58" r="24" :fill="`url(#${mintId})`" />
      <path d="M22 28h28l8 16H14l8-16Z" :fill="`url(#${blueId})`" />
      <path d="M18 44h36v22a8 8 0 0 1-8 8H26a8 8 0 0 1-8-8V44Z" :fill="`url(#${blueId})`" />
      <path d="M36 38c8 0 14 6 14 14H22c0-8 6-14 14-14Z" fill="#EFF6FF" />
      <path d="M28 54c4.5-4 11.5-4 16 0M31 59c3-2.4 7-2.4 10 0" stroke="#fff" stroke-width="2.2" stroke-linecap="round" />
      <circle cx="36" cy="63" r="2.2" fill="#fff" />
    </g>

    <g v-else-if="name === 'cloud'">
      <ellipse cx="58" cy="60" rx="24" ry="18" :fill="`url(#${mintId})`" />
      <path d="M24 50c0-11 8-18 18-18 6 0 12 3 15 8h3c8 0 14 6 14 13s-6 14-14 14H28c-8 0-14-6-14-13 0-6 4-11 10-12Z" :fill="`url(#${blueId})`" />
      <path d="M34 50h8M36 56h14" stroke="#fff" stroke-width="2.4" stroke-linecap="round" />
      <path d="M52 47h8M56 43v8" stroke="#fff" stroke-width="2.2" stroke-linecap="round" />
    </g>

    <g v-else-if="name === 'security'">
      <circle cx="58" cy="58" r="24" :fill="`url(#${mintId})`" />
      <circle cx="36" cy="38" r="22" :fill="`url(#${blueId})`" />
      <path d="M36 24c8 4 13 4 16 4v12c0 10-7 16-16 19-9-3-16-9-16-19V28c3 0 8 0 16-4Z" fill="#EFF6FF" />
      <circle cx="36" cy="40" r="4" fill="#2563EB" />
      <path d="M24 40h24M36 28v24" stroke="#2563EB" stroke-width="1.4" opacity=".35" />
    </g>

    <g v-else>
      <path d="M50 34h24v32a12 12 0 0 1-12 12H50V34Z" :fill="`url(#${mintId})`" />
      <path d="M20 22h36v44a10 10 0 0 1-10 10H30A10 10 0 0 1 20 66V22Z" :fill="`url(#${blueId})`" />
      <path d="M38 34c8 3 12 3 14 3v12c0 9-6 14-14 16-8-2-14-7-14-16V37c2 0 6 0 14-3Z" fill="#EFF6FF" />
      <circle cx="38" cy="48" r="5" fill="#2563EB" />
      <path d="M38 46v8" stroke="#fff" stroke-width="2" stroke-linecap="round" />
    </g>
  </svg>
</template>

<style scoped>
.icon {
  width: 72px;
  height: 72px;
}
</style>
