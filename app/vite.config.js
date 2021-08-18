import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";

import path from "path";

// const srcPath = path.resolve(__dirname, 'src/assets/styles', 'variables.scss')

// https://vitejs.dev/config/
export default ({ mode }) => {
  return defineConfig({
    plugins: [vue()],
    define: { "process.env": { ...process.env, ...loadEnv(mode, process.cwd()) } },
    resolve: {
      alias: {
        "@": path.join(__dirname, "src"),
        "@components": path.join(__dirname, "src/components"),
        "@views": path.join(__dirname, "src/views"),
        "@layouts": path.join(__dirname, "src/layouts"),
        "@pages": path.join(__dirname, "src/pages"),
        "@assets": path.join(__dirname, "src/assets"),
      },
    },
    /* remove the need to specify .vue files https://vitejs.dev/config/#resolve-extensions
    resolve: {
      extensions: [
        '.js',
        '.json',
        '.jsx',
        '.mjs',
        '.ts',
        '.tsx',
        '.vue',
      ]
    },
    */
  });
};
