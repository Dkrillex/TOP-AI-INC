<script setup>
import { computed, reactive, ref } from 'vue'
import { brand } from '@/config/brand'
import { useI18n } from '@/i18n'
import AppButton from '@/components/common/AppButton.vue'
import ContactIcon from '@/components/common/ContactIcon.vue'

const { t, messages } = useI18n()
const form = reactive({
  name: '',
  phone: '',
  email: '',
  message: '',
})
const submitted = ref(false)
const error = ref('')

const values = {
  email: brand.email,
  hours: brand.businessHours,
  address: brand.address,
}

const hrefs = {
  email: brand.emailHref,
}

const infoCards = computed(() =>
  messages.value.contact.cards.map((item) => ({
    ...item,
    value: values[item.key],
    href: hrefs[item.key],
  })),
)

function submit() {
  error.value = ''
  if (!form.name.trim() || !form.email.includes('@')) {
    error.value = t('contact.error')
    return
  }
  submitted.value = true
}
</script>

<template>
  <section class="contact-hero bg-grid">
    <div class="page-wrap hero-grid">
      <div class="copy">
        <p class="span-inter-500 kicker">{{ t('contact.kicker') }}</p>
        <h1 class="span-inter-800 title">{{ t('contact.title') }}</h1>
        <p class="span-poppins-400 subtitle">
          {{ t('contact.subtitle') }}
        </p>
        <a class="span-inter-800 phone" :href="brand.emailHref">{{ brand.email }}</a>
        <div class="actions">
          <AppButton to="/contact#message" variant="primary" arrow>{{ t('contact.send') }}</AppButton>
        </div>
      </div>
      <div class="visual">
        <img src="/images/contact-hero.png" alt="Talk with the Top AI team" />
      </div>
    </div>
  </section>

  <section class="contact-info">
    <div class="page-wrap">
      <p class="span-poppins-400 note">
        {{ t('contact.note') }}
      </p>
      <div class="info-grid">
        <article v-for="item in infoCards" :key="item.title" class="info-card">
          <ContactIcon :name="item.icon" />
          <div>
            <h3 class="span-inter-700">{{ item.title }}</h3>
            <a v-if="item.href" :href="item.href">{{ item.value }}</a>
            <p v-else>{{ item.value }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="contact-form-wrap">
    <div class="page-wrap">
      <form id="message" class="form" @submit.prevent="submit">
        <h2 class="span-inter-800">{{ t('contact.formTitle') }}</h2>
        <p class="span-poppins-400 hint">
          {{ t('contact.formHint') }}
        </p>
        <div class="row">
          <label>
            {{ t('contact.name') }}
            <input v-model="form.name" required />
          </label>
          <label>
            {{ t('contact.phone') }}
            <input v-model="form.phone" />
          </label>
        </div>
        <label>
          {{ t('contact.email') }}
          <input v-model="form.email" type="email" required />
        </label>
        <label>
          {{ t('contact.help') }}
          <textarea v-model="form.message" rows="5" :placeholder="t('contact.placeholder')" />
        </label>
        <p v-if="error" class="error">{{ error }}</p>
        <p v-if="submitted" class="ok">{{ t('contact.ok') }}</p>
        <AppButton type="submit" variant="primary" arrow>{{ t('contact.submit') }}</AppButton>
      </form>
    </div>
  </section>
</template>

<style scoped>
.contact-hero {
  position: relative;
  background-color: #fff;
}

.hero-grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 48px;
  align-items: center;
  min-height: 440px;
  padding: 72px 0;
}

.copy {
  max-width: 560px;
}

.visual {
  display: flex;
  align-items: center;
  justify-content: center;
}

.visual img {
  display: block;
  width: 100%;
  height: auto;
  max-height: 400px;
  object-fit: contain;
  object-position: center;
}

.kicker {
  display: inline-flex;
  margin: 0 0 16px;
  padding: 5px 12px;
  border: 1px solid #e2e8f0;
  border-radius: 999px;
  background: #fff;
  color: #475569;
  font-size: 12px;
}

.title {
  margin: 0 0 12px;
  max-width: 560px;
  font-size: 44px;
  line-height: 1.15;
  letter-spacing: -0.03em;
}

.subtitle {
  margin: 0 0 20px;
  max-width: 480px;
  color: var(--t-text-disable-color);
  font-size: 16px;
  line-height: 1.7;
}

.phone {
  display: block;
  color: var(--primary-text-color);
  font-size: 28px;
  letter-spacing: -0.02em;
}

.actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.contact-info {
  padding: 56px 0 8px;
}

.note {
  margin: 0 0 28px;
  max-width: 720px;
  color: var(--t-text-disable-color);
  line-height: 1.7;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.info-card {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  padding: 22px 20px;
}

.info-card h3 {
  margin: 0 0 6px;
  font-size: 14px;
  color: var(--t-text-disable-color);
  font-weight: 600;
}

.info-card a,
.info-card p {
  margin: 0;
  color: var(--primary-text-color);
  line-height: 1.6;
  font-size: 15px;
}

.info-card a:hover {
  color: var(--primary-default-color);
}

.contact-form-wrap {
  padding: 32px 0 var(--section-y);
}

.form {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-xl);
  padding: 40px 40px 36px;
  scroll-margin-top: 88px;
}

.form h2 {
  margin: 0 0 8px;
  font-size: 28px;
}

.hint {
  margin: 0 0 8px;
  color: var(--t-text-disable-color);
  line-height: 1.7;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

label {
  display: block;
  margin: 16px 0 0;
  font-size: 13px;
  font-weight: 600;
}

input,
textarea {
  display: block;
  width: 100%;
  margin-top: 8px;
  border: 1px solid var(--grey-color);
  border-radius: 12px;
  padding: 12px 14px;
  font-size: 14px;
  outline: none;
  background: #fff;
}

textarea {
  resize: vertical;
  min-height: 128px;
}

input:focus,
textarea:focus {
  border-color: var(--primary-default-color);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.08);
}

.error {
  color: #c0392b;
  margin: 12px 0 0;
}

.ok {
  color: #079248;
  margin: 12px 0 0;
}

.form :deep(.bubble-button) {
  margin-top: 24px;
}

@media (max-width: 860px) {
  .hero-grid,
  .info-grid,
  .row {
    grid-template-columns: 1fr;
  }

  .hero-grid {
    min-height: auto;
    padding: 48px 0 40px;
  }

  .title {
    font-size: 34px;
  }

  .visual img {
    max-height: 260px;
  }

  .form {
    padding: 28px 20px;
  }
}
</style>
