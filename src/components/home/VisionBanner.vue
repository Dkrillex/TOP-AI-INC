<script setup>
import AppButton from '@/components/common/AppButton.vue'
import { useI18n } from '@/i18n'

const { t } = useI18n()
</script>

<template>
  <section class="vision">
    <div class="page-wrap">
      <div class="box">
        <div>
          <p class="span-inter-500 eyebrow">{{ t('vision.eyebrow') }}</p>
          <h2 class="span-inter-800 title">
            {{ t('vision.title') }}
          </h2>
        </div>
        <AppButton to="/contact" variant="light" arrow>{{ t('common.book') }}</AppButton>
      </div>
    </div>
  </section>
</template>

<style scoped>
.vision {
  padding: 0 0 var(--section-y);
}

.box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  padding: 56px 48px;
  border-radius: 28px;
  background:
    radial-gradient(circle at 88% 20%, rgba(96, 165, 250, 0.35), transparent 36%),
    linear-gradient(180deg, #12233f 0%, #0b1220 100%);
  color: #fff;
}

.eyebrow {
  display: inline-flex;
  margin: 0 0 12px;
  padding: 5px 12px;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 999px;
  color: #bfdbfe;
  font-size: 12px;
}

.title {
  margin: 0;
  max-width: 640px;
  font-size: 28px;
  line-height: 1.3;
  letter-spacing: -0.03em;
}

@media (max-width: 768px) {
  .box {
    flex-direction: column;
    align-items: flex-start;
    padding: 36px 24px;
  }

  .title {
    font-size: 22px;
  }
}
</style>
