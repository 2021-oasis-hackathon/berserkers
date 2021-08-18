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
              개인 프로그램에 참여해보세요!
            </h2>
            <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
              서로 관심사가 맞는 사람들끼리 모여 새로운 프로그램을 기획하거나<br />
              사람들이 만든 프로그램에 참여하여 지역 공동체와 매칭을 할 수
              있습니다.<br />
              당신만의 프로그램에 참여보세요!
            </p>
            <div class="mt-12">
              <a
                href=""
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
              취미 맞는 사람과 함께 떠나 볼까요?
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in filterByKeyword('취미')" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <personal-program-card :item="item" />
          </div>
        </div>
        <div class="flex flex-wrap justify-flex-start mt-12 mb-2">
          <div class="w-full flex flex-row justify-between items-end px-4">
            <h2 class="text-3xl font-semibold text-nowrap">
              바쁜 일상 속 힐링이 필요할 땐
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in filterByKeyword('힐링')" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <personal-program-card :item="item" />
          </div>
        </div>

        <div class="flex flex-wrap justify-flex-start mt-12 mb-2">
          <div class="w-full flex flex-row justify-between items-end px-4">
            <h2 class="text-3xl font-semibold text-nowrap">
              마음이 따뜻해지는 봉사
            </h2>
          </div>
        </div>
        <div class="flex flex-wrap">
          <!-- TODO: 아 인덱스로 키 잡으면 안되는데 시간없다 -->
          <div v-for="(item, index) in filterByKeyword('봉사')" :key="index" class="mt-4 mb-4 px-2 lg:w-3/12 md:w-4/12 sm:w-6/12" >
            <personal-program-card :item="item" />
          </div>
        </div>
      </div>
    </section>
  </main>
  <footer-component />
</template>
<script>
import { computed, ref, onMounted } from "vue";
import { getAllPersonalProgram } from "@/firebase";

import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";
import PersonalProgramCard from "@components/Cards/PersonalProgramCard.vue";

import bannerImg from "@assets/images/banner003.jpg";
import componentBtn from "@assets/img/component-btn.png";

import useViewport from "@/hooks/useViewport.ts";

export default {
  setup() {
    const { type } = useViewport();

    const personalPrograms = ref([]);

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

    const filterByKeyword = keyword =>
      personalPrograms.value.filter((e) => e.keywords.find((k) => k === keyword ) !== undefined);

    onMounted(async () => {
      const _personalPrograms = await getAllPersonalProgram();
      personalPrograms.value = _personalPrograms;
    });

    return {
      personalPrograms,
      bannerImg,
      componentBtn,
      carouselSize,
      filterByKeyword
    };
  },
  components: {
    Navbar,
    FooterComponent,
    PersonalProgramCard,
  },
};
</script>
