import { defineConfig } from '@playwright/test'
const previewOrigin = 'http://127.0.0.1:4173'
const base = process.env.WIKI_BASE || '/'
export default defineConfig({
  testDir:'./tests', fullyParallel:false, workers:1, timeout:45000,
  reporter:'list', outputDir:'test-results',
  use:{ baseURL:previewOrigin, browserName:'chromium', channel:process.env.CI ? undefined : 'chrome', headless:true, screenshot:'only-on-failure' },
  webServer:{ command:'npm run preview -- --host 127.0.0.1 --port 4173', url:previewOrigin+base, reuseExistingServer:false, timeout:30000 }
})
