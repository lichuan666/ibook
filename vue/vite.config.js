import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
    base: "./",       //新加
    plugins: [vue()],
    
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)),          //原版
            //"/img":"./src/assets",          //新加
        }
    },
    //新加

    build: {
        chunkSizeWarningLimit:1500,
        outDir: 'dist',
        assetsDir: 'assets',
        //assetsDir: 'static/img/'
    },

    proxyTable: {
        "/api":{
          target: 'http://localhost:8080',      //后端接口的根目录
          changeOrigin: true,                    //是否跨域
          pathRewrite: {
              '^/api': ''
          }
        }
      }
  
})

