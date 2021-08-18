<template>
  <carousel>
    <slide v-for="item in items" :key="item.id">
      <slot :item="item"></slot>
    </slide>
    <template #addons>
      <navigation>
      </navigation>
    </template>
  </carousel>
</template>

<style>
.carousel__prev,
.carousel__next {
	border: 1px solid lightgray;
	background-color: white;
    color: rgb(34, 34, 34)
}
</style>

<script lang="ts">
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";

export default {
  props: {
    items: {
      type: Array as () => Array<any>,
      required: true,
      default: () => [],
    },
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
};
</script>
