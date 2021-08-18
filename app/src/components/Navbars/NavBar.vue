<template>
  <nav
    :class="isScrollable && 'shadow'"
    class="
      top-0
      fixed
      z-50
      w-full
      flex flex-wrap
      items-center
      justify-between
      px-2
      py-2
      navbar-expand-lg
      bg-white
    "
    :style="{
      backgroundColor: isScrollable ? 'white' : 'transparent',
      transition: '0.2s ease-out',
    }"
  >
    <div
      class="container px-4 mx-auto flex flex-wrap items-center justify-between"
    >
      <div
        class="
          w-full
          relative
          flex
          justify-between
          lg:w-auto lg:static lg:block lg:justify-start
        "
      >
        <router-link to="/" class="logo">
          <icon-base
            viewBox="0 0 50 50"
            width="70"
            height="70"
            :iconColor="
              isScrollable ? 'rgba(5, 150, 105, 1)' : 'rgba(255,255,255,1)'
            "
            icon-name="logo"
          >
            <logo></logo>
          </icon-base>
        </router-link>
        <button
          class="
            cursor-pointer
            text-xl
            leading-none
            px-3
            py-1
            border border-solid border-transparent
            rounded
            bg-transparent
            block
            lg:hidden
            outline-none
            focus:outline-none
          "
          type="button"
          v-on:click="toggle"
        >
          <i class="fas fa-bars"></i>
        </button>
      </div>
      <div
        class="lg:flex flex-grow items-center"
        :class="[isOpened ? 'block' : 'hidden']"
        id="example-navbar-warning"
      >
        <ul class="flex flex-col lg:flex-row list-none lg:ml-auto">
          <li class="flex items-center mr-3">
            <router-link
              to="/personal-programs"
              :class="
                isScrollable
                  ? 'hover:text-blueGray-500 text-blueGray-900'
                  : 'hover:text-blueGray-300 text-blueGray-100'
              "
              class="px-3 py-2 text-md"
            >
              개인 프로그램
            </router-link>
          </li>
          <li class="flex items-center mr-3">
            <router-link
              to="/local-community-programs"
              :class="
                isScrollable
                  ? 'hover:text-blueGray-500 text-blueGray-900'
                  : 'hover:text-blueGray-300 text-blueGray-100'
              "
              class="px-3 py-2 text-md"
            >
              지역 공동체 프로그램
            </router-link>
          </li>
          <li class="flex items-center mr-3">
            <router-link
              to="/program-management"
              :class="
                isScrollable
                  ? 'hover:text-blueGray-500 text-blueGray-900'
                  : 'hover:text-blueGray-300 text-blueGray-100'
              "
              class="px-3 py-2 text-md"
            >
              프로그램 관리
            </router-link>
          </li>
        </ul>
        <ul class="flex flex-col lg:flex-row list-none lg:ml-auto">
          <li class="flex items-center">
            <button
              class="
                bg-emerald-500
                text-white
                active:bg-emerald-600
                text-xs
                font-bold
                uppercase
                px-4
                py-2
                rounded
                shadow
                hover:shadow-lg
                outline-none
                focus:outline-none
                lg:mr-1 lg:mb-0
                ml-3
                mb-3
                ease-linear
                transition-all
                duration-150
              "
              type="button"
            >
              <i class="fas fa-arrow-alt-circle-down"></i> 지역 공동체 등록
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.logo {
  width: 70px;
  height: 70px;
}
</style>

<script>
import { ref, reactive, onMounted, computed } from "vue";

import IconBase from "@components/Icon/IconBase.vue";
import Logo from "@components/Icon/Logo.vue";

const useToggle = () => {
  const isOpened = ref(false);
  const toggle = () => (isOpened.value = !isOpened.value);

  return { isOpened, toggle };
};

export default {
  props: {
    content: {
      type: Boolean,
      default: false,
    },
  },
  setup({content}) {
    const { isOpened, toggle } = useToggle();
    const scrollPosition = ref(0);
    const isScrollable = computed(() => content || scrollPosition.value > 300);

    onMounted(() => {
      window.addEventListener(
        "scroll",
        () => (scrollPosition.value = window.scrollY)
      );
    });

    return { isOpened, toggle, isScrollable };
  },
  components: {
    IconBase,
    Logo,
  },
};
</script>
