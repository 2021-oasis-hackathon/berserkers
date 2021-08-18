<template>
  <div>
    <navbar />
    <main>
      <div
        class="
          relative
          pt-16
          pb-32
          flex
          content-center
          items-center
          justify-center
          min-h-screen-75
        "
      >
        <div
          class="absolute top-0 w-full h-full bg-center bg-no-repeat bg-cover"
          style="background-image: url('/src/assets/images/banner005.jpg'); background-color: #feead2;"
        >
          <span
            id="blackOverlay"
            class="w-full h-full absolute bg-black opacity-75"
          ></span>
        </div>
        <div class="container relative mx-auto">
          <div class="items-center flex flex-wrap">
            <div class="w-full lg:w-5/12 px-4 ml-auto mr-auto mb-3 text-center">
              <div class="pr-12">
                <h1 class="text-blueGray-200 font-semibold text-4xl">
                  호남이 시나브로 활기차지게, 호나므로
                </h1>
                <p class="mt-4 mb-5 text-lg text-blueGray-300">
                  청년 x 지역공동체 한달살이 프로그램 매칭 플랫폼
                </p>
              </div>
            </div>
          </div>
        </div>
        <div
          class="
            top-auto
            bottom-0
            left-0
            right-0
            w-full
            absolute
            pointer-events-none
            overflow-hidden
            h-70-px
          "
          style="transform: translateZ(0)"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="fill-current"
              style="color: #f5f7f6;"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </div>

      <section
        class="header relative pt-16 items-center flex h-screen max-h-860-px"
        style="background-color: #f5f7f6;"
      >
        <div class="container mx-auto items-center flex flex-wrap">
          <div class="w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4">
            <div class="pt-32 sm:pt-0">
              <h2 class="font-semibold text-4xl text-blueGray-600">
                마음 맞는 사람들과 함께<br/>
                한달살이에 도전해보세요!
              </h2>
              <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
                지역 공동체에서 제공해주는 프로그램 뿐만 아니라<br/>
                다양한 사람들과 모여 기획하고 마을과 연계하여 <br/>
                한달살이를 진행할 수 있습니다.
              </p>
              <div class="mt-12">
                <a
                  href="https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-index"
                  target="_blank"
                  class="
                    get-started
                    text-white
                    font-bold
                    px-6
                    py-4
                    rounded
                    outline-none
                    focus:outline-none
                    mr-1
                    mb-1
                    bg-emerald-500
                    active:bg-emerald-600
                    uppercase
                    text-sm
                    shadow
                    hover:shadow-lg
                    ease-linear
                    transition-all
                    duration-150
                  "
                >
                  모임 생성
                </a>
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
                  모임 알아보기
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
            max-h-860-px
          "
          :src="bannerImg"
          alt="..."
        />
      </section>
    </main>
    <footer-component />
  </div>
</template>
<script>
import { reactive, onMounted } from 'vue';
import { getAllPersonalProgram } from "@/firebase"

import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";

import bannerImg from "@assets/images/banner004.jpg";
import componentBtn from "@assets/img/component-btn.png";

export default {
  setup() {
    const personalPrograms = reactive([]);

    onMounted(async () => {
      const programs = await getAllPersonalProgram();
      console.log(programs);
      // personalPrograms = programs;
    })

    return { personalPrograms, bannerImg, componentBtn }
  },
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>
