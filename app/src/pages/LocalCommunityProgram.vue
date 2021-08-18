<template>
  <navbar content />
  <main>
    <section
      class="header relative pt-16 items-center flex h-screen max-h-650-px border-b"
    >
      <div class="container mx-auto items-center flex flex-wrap">
        <div class="w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4">
          <div class="pt-32 sm:pt-0">
            <h2 class="font-semibold text-4xl text-blueGray-600">
              지역 공동체 프로그램
            </h2>
            <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
              호남 지역의 마을, 지자체, 단체들이 기획한 한달살이 프로그램에 
              도전해보실 수 있습니다. 프로그램마다 관심사, 지역, 테마들이 
              다양하고 지역 공동체에서 여러분의 활동을 지원해줍니다.
            </p>
            <div class="mt-12">
              <a
                href="https://github.com/creativetimofficial/vue-notus?ref=vn-index"
                class="
                  github-star
                  ml-1
                  text-white
                  font-bold
                  px-6
                  py-4
                  rounded
                  outline-none
                  focus:outline-none
                  mr-1
                  mb-1
                  bg-blueGray-700
                  active:bg-blueGray-600
                  uppercase
                  text-sm
                  shadow
                  hover:shadow-lg
                  ease-linear
                  transition-all
                  duration-150
                "
                target="_blank"
              >
                둘러보기
              </a>
            </div>
          </div>
        </div>
      </div>

      <img
        class="
          absolute
          top-0
          b-auto
          right-0
          pt-16
          sm:w-6/12
          -mt-48
          sm:mt-0
          w-10/12
          max-h-650-px
        "
        :src="bannerImg"
        alt="..."
      />
    </section>
    
    <section class="pt-20 pb-48 bg-blueGray-100">
      <div class="container mx-auto px-4">
        <div class="flex flex-wrap justify-flex-start mb-2">
          <div class="w-full flex flex-row justify-between items-end px-4">
            <h2 class="text-3xl font-semibold text-nowrap">
              전남이 예술이랑께
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in localCommunityPrograms" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <local-community-program-card :item="item" />
          </div>
        </div>
        <div class="flex flex-wrap justify-flex-start mt-12 mb-2">
          <div class="w-full flex flex-row justify-between items-end px-4">
            <h2 class="text-3xl font-semibold text-nowrap">
              호남은 여러분들을 위해 열려 있습니다.
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in localCommunityPrograms" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <local-community-program-card :item="item" />
          </div>
        </div>

        <div class="flex flex-wrap justify-flex-start mt-12 mb-2">
          <div class="w-full flex flex-row justify-between items-end px-4">
            <h2 class="text-3xl font-semibold text-nowrap">
              청년들로 시나브로 호남이 활기차게
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in localCommunityPrograms" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <local-community-program-card :item="item" />
          </div>
        </div>
      </div>
    </section>
  </main>
  <footer-component />
</template>
<script>
import { computed, ref, onMounted } from "vue";
import { getAllLocalCommunityProgram } from "@/firebase";

import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";
import LocalCommunityProgramCard from "@components/Cards/LocalCommunityProgramCard.vue";

import bannerImg from "@assets/images/banner002.jpg";
import componentBtn from "@assets/img/component-btn.png";

import useViewport from "@/hooks/useViewport.ts";

export default {
  setup() {
    const { type } = useViewport();

    const localCommunityPrograms = ref([]);

    const carouselSize = computed(() => {
      switch (type.value) {
        case "xs":
          return 1;
        case "sm":
          return 2;
        case "md":
          return 3;
        case "lg":
          return 4;
      }
    });

    onMounted(async () => {
      const _localCommunityPrograms = await getAllLocalCommunityProgram();
      localCommunityPrograms.value = _localCommunityPrograms;
    });

    return {
      localCommunityPrograms,
      bannerImg,
      componentBtn,
      carouselSize,
    };
  },
  components: {
    Navbar,
    FooterComponent,
    LocalCommunityProgramCard,
  },
};
</script>
