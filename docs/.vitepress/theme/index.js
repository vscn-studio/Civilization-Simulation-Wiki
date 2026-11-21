import DefaultTheme from 'vitepress/theme'
import './style.css'
import FoodCatalogue from './FoodCatalogue.vue'
import ModCatalogue from './ModCatalogue.vue'
import PortalCards from './PortalCards.vue'
import { onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('FoodCatalogue', FoodCatalogue)
    app.component('ModCatalogue', ModCatalogue)
    app.component('PortalCards', PortalCards)
  },
  setup() {
    const route = useRoute()
    const reveal = async () => {
      await nextTick()
      let id
      try { id = decodeURIComponent(location.hash.slice(1)) } catch { return }
      const target = document.getElementById(id)
      if (!target) return
      let p = target.parentElement, opened = false
      while (p) { if (p.tagName === 'DETAILS') { p.open = true; opened = true } p = p.parentElement }
      if (opened) target.scrollIntoView({ block:'start' })
    }
    onMounted(() => { window.addEventListener('hashchange', reveal); reveal() })
    onUnmounted(() => window.removeEventListener('hashchange', reveal))
    watch(() => route.path, () => { if (typeof window !== 'undefined') reveal() }, { flush:'post' })
  }
}
