import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import legacy from '@vitejs/plugin-legacy'

// https://vite.dev/config/
export default defineConfig({
  build: {
    assetsInlineLimit: 5 * 1024,
    rollupOptions: {
      external: ['abortcontroller-polyfill/dist/polyfill-patch-fetch'],
    },
  },
  plugins: [vue(),
  legacy({
    targets: ['defaults', 'fully supports es6'],
  })],
})