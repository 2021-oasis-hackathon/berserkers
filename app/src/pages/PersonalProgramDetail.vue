<template>
  <navbar content />
  <main class="mt-20">
    <div
      class="
        relative
        pt-16
        pb-16
        flex
        content-center
        items-center
        justify-center
        min-h-screen-15
      "
    >
      <div
        class="absolute top-0 w-full h-full bg-center bg-no-repeat bg-cover"
        style="
          background-image: url('https://images.unsplash.com/photo-1567619435005-4d3be491538d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8OTB8fG11cmFsfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60');
          background-color: #feead2;
        "
      >
        <span
          id="blackOverlay"
          class="w-full h-full absolute bg-black opacity-75"
        ></span>
      </div>
      <div class="container relative mx-auto mt-10">
        <div class="items-center flex flex-wrap">
          <div class="w-full lg:w-5/12 px-4 ml-auto mr-auto text-center">
            <div class="pr-12">
              <h1 class="text-blueGray-200 font-semibold text-4xl">
                벽에 따뜻한 마음을 그려요
              </h1>
              <p class="mt-4 mb-5 text-lg text-blueGray-300">
                호남 지역에서 벽화 그리는 프로그램 기획
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-wrap pt-12 pb-40 container mx-auto">
      <div class="w-full lg:w-8/12 px-4">
        <PersonalProgramContentCard />
      </div>
      <div class="w-full lg:w-4/12 px-4">
        <PersonalProgramInfoCard />
      </div>
    </div>
  </main>
  <footer-component />
</template>

<script>
import { ref } from "vue";

import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";
import PersonalProgramContentCard from "@/components/Cards/PersonalProgramContentCard.vue";
import PersonalProgramInfoCard from "@/components/Cards/PersonalProgramInfoCard.vue";

import bannerImg from "@assets/images/banner002.jpg";
import componentBtn from "@assets/img/component-btn.png";

export default {
  setup() {
    return {
      bannerImg,
      componentBtn,
    };
  },
  components: {
    Navbar,
    FooterComponent,
    PersonalProgramContentCard,
    PersonalProgramInfoCard,
  },
};
</script>
