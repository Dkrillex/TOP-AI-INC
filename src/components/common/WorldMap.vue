<script setup>
import { useId } from 'vue'

defineProps({
  alt: { type: String, default: 'Top AI global network' },
})

// Coordinates are in the base image space (1536 x 1024).
const nodes = [
  { id: 'sanFrancisco', x: 207, y: 457 },
  { id: 'london', x: 717, y: 367 },
  { id: 'frankfurt', x: 781, y: 394 },
  { id: 'singapore', x: 1164, y: 643 },
  { id: 'tokyo', x: 1340, y: 452 },
]

const routes = [
  'M 207 457 Q 462 300 717 367',
  'M 207 457 Q 500 352 781 394',
  'M 207 457 Q 685 430 1164 643',
  'M 781 394 Q 999 127 1340 452',
  'M 1164 643 Q 1330 570 1340 452',
]

const glowId = `world-map-glow-${useId()}`
</script>

<template>
  <div class="world-map">
    <img class="world-map-base" src="/images/world-map-base.png" :alt="alt" />
    <svg class="world-map-routes" viewBox="0 0 1536 1024" fill="none" aria-hidden="true">
      <defs>
        <radialGradient :id="glowId">
          <stop offset="35%" stop-color="#2f80f7" stop-opacity="0.38" />
          <stop offset="100%" stop-color="#2f80f7" stop-opacity="0" />
        </radialGradient>
      </defs>
      <g stroke="#0b7cf5" stroke-linecap="round">
        <path v-for="d in routes" :key="`glow-${d}`" :d="d" stroke-width="11" stroke-opacity="0.12" />
        <path v-for="d in routes" :key="d" :d="d" stroke-width="3" />
      </g>
      <g v-for="node in nodes" :key="node.id">
        <circle :cx="node.x" :cy="node.y" r="36" :fill="`url(#${glowId})`" />
        <circle :cx="node.x" :cy="node.y" r="16.5" fill="#ffffff" />
        <circle :cx="node.x" :cy="node.y" r="10.5" fill="#0b7cf5" />
      </g>
    </svg>
  </div>
</template>

<style scoped>
.world-map {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.world-map-base,
.world-map-routes {
  display: block;
  width: 100%;
}

.world-map-routes {
  position: absolute;
  inset: 0;
  height: 100%;
}
</style>
