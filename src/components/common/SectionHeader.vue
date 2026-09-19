<script setup>
defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  desc: { type: String, default: '' },
  align: { type: String, default: 'center' },
})
</script>

<template>
  <div class="section-header" :class="align">
    <p v-if="eyebrow" class="span-inter-500 eyebrow">{{ eyebrow }}</p>
    <h2 class="span-inter-800 title">{{ title }}</h2>
    <p v-if="desc" class="span-poppins-400 desc">{{ desc }}</p>
  </div>
</template>

<style scoped>
.section-header {
  display: flex;
  flex-direction: column;
  margin-bottom: 40px;
}

.section-header.center {
  align-items: center;
  text-align: center;
}

.section-header.left {
  align-items: flex-start;
  text-align: left;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  margin: 0 0 14px;
  padding: 5px 12px;
  border: 1px solid #e4e4e7;
  border-radius: 999px;
  background: #fff;
  color: #52525b;
  font-size: 12px;
  letter-spacing: 0.01em;
}

.title {
  margin: 0;
  font-size: 36px;
  line-height: 1.2;
  letter-spacing: -0.03em;
  color: var(--primary-text-color);
}

.desc {
  margin: 14px 0 0;
  max-width: 640px;
  color: var(--t-text-disable-color);
  font-size: 16px;
  line-height: 1.7;
}

@media (max-width: 768px) {
  .title {
    font-size: 28px;
  }
}
</style>
