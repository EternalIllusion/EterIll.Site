import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import legacy from '@vitejs/plugin-legacy'

// https://vite.dev/config/
export default defineConfig({
  build: {
    assetsInlineLimit: 5 * 1024,
    rollupOptions: {
      external: ['abortcontroller-polyfill/dist/polyfill-patch-fetch'],
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor';
          }
        }
      }
    },
  },
  plugins: [vue(),
  legacy({
    targets: ['defaults', 'fully supports es6'],
  })],
})