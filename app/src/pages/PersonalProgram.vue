<template>
    <navbar content />
    <main>
      <section
        class="header relative pt-16 items-center flex h-screen max-h-860-px"
      >
        <div class="container mx-auto items-center flex flex-wrap">
          <div class="w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4">
            <div class="pt-32 sm:pt-0">
              <h2 class="font-semibold text-4xl text-blueGray-600">
                개인 프로그램에 참여해보세요!
              </h2>
              <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
                서로 관심사가 맞는 사람들끼리 모여 새로운 프로그램을 기획하거나<br/>
                사람들이 만든 프로그램에 참여하여 지역 공동체와 매칭을 할 수 있습니다.<br/>
                당신만의 프로그램에 참여보세요!
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
            max-h-860-px
          "
          :src="bannerImg"
          alt="..."
        />
      </section>
    </main>
    <footer-component />
</template>
<script>
import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";

import bannerImg from "@assets/images/banner003.jpg";
import componentBtn from "@assets/img/component-btn.png";

export default {
  data() {
    return {
      bannerImg,
      componentBtn,
    };
  },
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>


