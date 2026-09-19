<script setup>
import { computed } from 'vue'
import { brand } from '@/config/brand'
import { useI18n } from '@/i18n'
import SectionHeader from '@/components/common/SectionHeader.vue'
import CapabilityIcon from '@/components/common/CapabilityIcon.vue'
import VisionBanner from '@/components/home/VisionBanner.vue'

const { t, messages } = useI18n()
const stats = computed(() => messages.value.about.stats)
const industries = computed(() => messages.value.about.industries)
</script>

<template>
  <section class="about-hero">
    <div class="sky">
      <div class="page-wrap sky-inner">
        <p class="span-inter-600 place">{{ t('about.place') }}</p>
      </div>
    </div>
    <div class="page-wrap">
      <div class="stats">
        <article v-for="item in stats" :key="item.label" class="stat">
          <p class="span-inter-800 value">{{ item.value }}</p>
          <p class="span-poppins-400 label">{{ item.label }}</p>
        </article>
      </div>
    </div>
  </section>

  <section class="about-intro">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('about.eyebrow')"
        :title="t('about.title')"
      />
      <p class="span-poppins-400 copy">
        {{ t('about.copy1', { name: brand.displayName }) }}
      </p>
      <p class="span-poppins-400 copy">
        {{ t('about.copy2') }}
      </p>
      <div class="visuals">
        <figure class="visual">
          <img src="/images/about-city.png" alt="Dallas registered office" />
          <figcaption class="span-inter-600">{{ t('about.hq') }}</figcaption>
        </figure>
        <figure class="visual">
          <img src="/images/about-license.png" alt="Texas for-profit corporation" />
          <figcaption class="span-inter-600">{{ t('about.license') }}</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="about-support">
    <div class="page-wrap">
      <SectionHeader
        align="left"
        :eyebrow="t('about.supportEyebrow')"
        :title="t('about.supportTitle')"
        :desc="t('about.supportDesc')"
      />
      <div class="cards">
        <article v-for="item in industries" :key="item.title" class="card">
          <CapabilityIcon :name="item.icon" />
          <h3 class="span-inter-700">{{ item.title }}</h3>
          <p class="span-poppins-400">{{ item.desc }}</p>
        </article>
      </div>
    </div>
  </section>

  <VisionBanner />
</template>

<style scoped>
.about-hero {
  position: relative;
  padding-bottom: 48px;
}

.sky {
  height: 380px;
  background:
    linear-gradient(180deg, transparent 42%, #fff 100%),
    url('/images/about-sf.png') center 35% / cover no-repeat;
  display: flex;
  align-items: flex-end;
}

.sky-inner {
  display: flex;
  justify-content: flex-end;
}

.place {
  margin: 0 0 88px;
  color: #fff;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35);
  letter-spacing: 0.04em;
}

.stats {
  margin-top: -72px;
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-xl);
  box-shadow: var(--card-shadow);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding: 32px 8px;
}

.stat {
  text-align: center;
  padding: 0 12px;
}

.stat:not(:last-child) {
  border-right: 1px solid var(--line-subtle);
}

.value {
  margin: 0;
  font-size: 36px;
  letter-spacing: -0.03em;
  color: var(--primary-text-color);
}

.label {
  margin: 8px 0 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
}

.about-intro {
  padding: 32px 0 var(--section-y);
}

.copy {
  max-width: 760px;
  margin: 0 0 16px;
  color: var(--t-text-disable-color);
  line-height: 1.8;
  font-size: 15px;
}

.visuals {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 36px;
}

.visual {
  margin: 0;
  border-radius: var(--radius-xl);
  overflow: hidden;
  background: #fff;
  border: 1px solid #e2e8f0;
}

.visual img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  display: block;
}

.visual figcaption {
  padding: 14px 18px 16px;
  font-size: 13px;
  color: var(--primary-text-color);
}

.about-support {
  padding: 24px 0 var(--section-y);
  background: #fff;
}

.cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.card {
  background: #fff;
  border: 1px solid var(--line-subtle);
  border-radius: var(--radius-lg);
  padding: 24px 20px 28px;
  text-align: left;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: var(--card-shadow);
}

.card h3 {
  margin: 12px 0 8px;
  font-size: 16px;
  line-height: 1.35;
}

.card :deep(.icon) {
  width: 56px;
  height: 56px;
}

.card p {
  margin: 0;
  color: var(--t-text-disable-color);
  font-size: 13px;
  line-height: 1.7;
}

@media (max-width: 960px) {
  .stats,
  .cards,
  .visuals {
    grid-template-columns: 1fr 1fr;
  }

  .stat:nth-child(2) {
    border-right: 0;
  }
}

@media (max-width: 640px) {
  .stats,
  .cards,
  .visuals {
    grid-template-columns: 1fr;
  }

  .stat:not(:last-child) {
    border-right: 0;
    border-bottom: 1px solid var(--line-subtle);
    padding: 16px 0;
  }
}
</style>
