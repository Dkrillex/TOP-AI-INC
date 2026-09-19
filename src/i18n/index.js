import { computed } from 'vue'
import en from './en'

function resolve(source, path) {
  return path.split('.').reduce((acc, key) => (acc == null ? acc : acc[key]), source)
}

export function useI18n() {
  const messages = computed(() => en)

  function t(path, vars = {}) {
    const raw = resolve(messages.value, path)
    if (typeof raw !== 'string') return path
    return raw.replace(/\{(\w+)\}/g, (_, key) => (vars[key] == null ? `{${key}}` : String(vars[key])))
  }

  return { messages, t }
}
