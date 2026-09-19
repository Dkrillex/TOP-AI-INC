<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'

const { t, messages } = useI18n()
const history = computed(() => messages.value.home.history)
</script>

<template>
  <section class="global-history">
    <div class="page-wrap">
      <SectionHeader align="left" :eyebrow="t('home.historyEyebrow')" :title="t('home.historyTitle')" />
      <div class="gh-body">
        <div class="timeline">
          <article v-for="item in history" :key="item.year" class="item">
            <p class="span-inter-700 year">{{ item.year }}</p>
            <h3 class="span-inter-700 title">{{ item.title }}</h3>
            <ul v-if="item.points.length">
              <li v-for="point in item.points" :key="point" class="span-poppins-400">{{ point }}</li>
            </ul>
          </article>
        </div>
        <div class="gh-map">
          <img class="map" src="/images/world-map.png" alt="Top AI global footprint" />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.global-history {
  padding: var(--section-y) 0;
  background: #fff;
}

.gh-body {
  display: grid;
  grid-template-columns: 0.92fr 1.08fr;
  gap: 48px;
  align-items: stretch;
}

.timeline {
  display: flex;
  flex-direction: column;
}

.item {
  position: relative;
  padding: 4px 0 28px 28px;
  border-left: 2px solid #bfdbfe;
}

.item:last-child {
  padding-bottom: 0;
}

.item::before {
  content: '';
  position: absolute;
  left: -7px;
  top: 8px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--primary-default-color);
  box-shadow: 0 0 0 4px #f8fafc;
}

.year {
  margin: 0 0 6px;
  color: var(--primary-default-color);
  font-size: 13px;
  letter-spacing: 0.08em;
}

.title {
  margin: 0 0 8px;
  font-size: 18px;
}

ul {
  margin: 0;
  padding-left: 18px;
  color: var(--t-text-disable-color);
  font-size: 13px;
  line-height: 1.75;
}

.gh-map {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-xl);
  padding: 20px;
  display: flex;
  align-items: center;
}

.map {
  width: 100%;
  border-radius: var(--radius-md);
  display: block;
}

@media (max-width: 860px) {
  .gh-body {
    grid-template-columns: 1fr;
  }
}
</style>
