import { createApp } from 'vue';
import { createWebHistory, createRouter } from 'vue-router';

import "@fortawesome/fontawesome-free/css/all.min.css";
// import "@assets/styles/index.css"
import "@assets/styles/tailwind.css";

import App from '@/App.vue';

import Index from '@/pages/Index.vue';
import PersonalProgram from '@/pages/PersonalProgram.vue';
import LocalCommunityProgram from '@/pages/LocalCommunityProgram.vue';
import ProgramManagement from '@/pages/ProgramManagement.vue';

const routes = [{
    path: "/",
    component: Index 
}, {
    path: "/personal-programs",
    component: PersonalProgram 
}, {
    path: "/local-community-programs",
    component: LocalCommunityProgram 
}, {
    path: "/program-management",
    component: ProgramManagement 
}];

const router = createRouter({
    history: createWebHistory(),
    routes
});

createApp(App).use(router).mount('#app');
