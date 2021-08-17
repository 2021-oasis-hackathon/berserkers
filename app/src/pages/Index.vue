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
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="background-image: url('/src/assets/images/main_banner.jpg')"
        >
          <span
            id="blackOverlay"
            class="w-full h-full absolute bg-black opacity-50"
          ></span>
        </div>
        <div class="container relative mx-auto">
          <div class="items-center flex flex-wrap">
            <div class="w-full lg:w-5/12 px-4 ml-auto mr-auto text-center">
              <div class="pr-12">
                <h1 class="text-white font-semibold text-5xl">
                  
                </h1>
                <p class="mt-4 text-lg text-blueGray-200">
                  
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
              class="text-white fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </div>


    </main>
    <footer-component />
  </div>
</template>
<script>
import Navbar from "@/components/Navbars/NavBar.vue";
import FooterComponent from "@components/Footers/Footer.vue";

import patternVue from "@assets/images/main_banner.jpg";
import componentBtn from "@assets/img/component-btn.png";

export default {
  data() {
    return {
      patternVue,
      componentBtn,
    };
  },
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>
