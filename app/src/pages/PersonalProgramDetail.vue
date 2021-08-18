<template>
    <navbar content />
    <main>
      
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
