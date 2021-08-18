<template>
  <div class="p-10">
    <!--Card 1-->
    <div
      class="max-w-sm rounded overflow-hidden shadow-lg text-left flex flex-col"
      style="height: 350px"
    >
      <img
        class="w-full"
        style="object-fit: cover; height: 150px"
        :src="item.imgUrl"
        alt="unknown"
      />
      <div class="flex flex-1 flex-col px-3 py-4">
        <div class="font-bold text-2xs mb-2">{{ item.title }}</div>
        <p class="text-gray-700 text-xs">
          {{ item.description }}
        </p>
      </div>
      <div class="px-3 py-2">
        
      </div>
      <div class="px-3 pt-4 pb-2">
        <span
          v-for="(item, index) in item.keywords"
          :key="index"
          class="
            inline-block
            bg-gray-200
            rounded-full
            px-3
            py-1
            text-sm
            font-semibold
            text-gray-700
            mr-2
            mb-2
          "
        >
          #{{ item }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    item: {
      type: Object as any,
      required: true,
    },
  },
};
</script>
