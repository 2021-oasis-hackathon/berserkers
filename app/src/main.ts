import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@assets/styles/tailwind.css";

import App from "@/App.vue";

import Index from "@pages/Index.vue";
import PersonalProgram from "@pages/PersonalProgram.vue";
import LocalCommunityProgram from "@pages/LocalCommunityProgram.vue";
import ProgramManagement from "@pages/ProgramManagement.vue";
import PersonalProgramDetail from "@pages/PersonalProgramDetail.vue";
import LocalCommunityProgramDetail from "@pages/LocalCommunityProgramDetail.vue";

const routes = [
  {
    path: "/",
    component: Index,
  },
  {
    path: "/personal-programs",
    component: PersonalProgram,
  },
  {
    path: '/personal-programs/:id',
    component: PersonalProgramDetail
  },
  {
    path: "/local-community-programs",
    component: LocalCommunityProgram,
  },
  {
    path: '/local-community-programs/:id',
    component: LocalCommunityProgramDetail
  },
  {
    path: "/program-management",
    component: ProgramManagement,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
