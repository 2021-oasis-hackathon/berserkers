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
          background-image: url('https://images.unsplash.com/photo-1501366062246-723b4d3e4eb6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=180');
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
                예술, 오 비엔날레
              </h1>
              <p class="mt-4 mb-5 text-lg text-blueGray-300">
                광주광역시 지역 공동체 프로그램
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-wrap pt-12 pb-40 container mx-auto">
      <div class="w-full lg:w-8/12 px-4">
        <LocalCommunityProgramContentCard />
      </div>
      <div class="w-full lg:w-4/12 px-4">
        <LocalCommunityProgramInfoCard />
      </div>
      <div class="container flex items-center mt-12 pb-24 px-4">
        <div id="disqus_thread" class="w-full"></div>
      </div>
    </div>
  </main>
  <footer-component />
</template>

<script>
import { ref, onMounted } from "vue";

import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";
import LocalCommunityProgramContentCard from "@/components/Cards/LocalCommunityProgramContentCard.vue";
import LocalCommunityProgramInfoCard from "@/components/Cards/LocalCommunityProgramInfoCard.vue";

import bannerImg from "@assets/images/banner002.jpg";
import componentBtn from "@assets/img/component-btn.png";

export default {
  setup() {
    const disqus_config = function () {
      this.page.url = 'http://203.254.143.193:3000/local-community-programs/test';  // Replace PAGE_URL with your page's canonical URL variable
      this.page.identifier = 'local-community-programs/test'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    
    (function () {
      // DON'T EDIT BELOW THIS LINE
      var d = document,
        s = d.createElement("script");
      s.src = "https://honameuro.disqus.com/embed.js";
      s.setAttribute("data-timestamp", +new Date());
      (d.head || d.body).appendChild(s);
    })();

    return {
      bannerImg,
      componentBtn,
    };
  },
  components: {
    Navbar,
    FooterComponent,
    LocalCommunityProgramContentCard,
    LocalCommunityProgramInfoCard,
  },
};
</script>
