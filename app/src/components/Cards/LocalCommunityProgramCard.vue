<template>
  <a :href="'/local-community-programs/' + item.id">
    <div class="p-10">
      <!--Card 1-->
      <div
        class="
          max-w-sm
          rounded
          overflow-hidden
          shadow-lg
          text-left
          flex flex-col flex-1 flex-wrap
        "
        style="height: 390px"
      >
        <img
          class="w-full"
          style="object-fit: cover; height: 150px"
          :src="data.imgUrl"
          alt="unknown"
        />
        <div class="flex flex-col flex-1 flex-wrap">
          <div class="flex flex-1 flex-col px-3 my-2">
            <div class="font-bold text-emerald-600 text-xs mb-1">
              <i class="fas fa-map-marker-alt"></i>
              {{ data.location.region }}
            </div>
            <div id="title" class="font-bold text-2xs mb-1">{{ data.title }}</div>
            <p id="description" class="text-gray-700 text-sm">
              {{ data.description }}
            </p>
          </div>
          <div class="flex flex-col px-3 my-2 text-gray-700">
            <div class="text-xs mb-2">
              <span class="font-bold">예정기간:</span> {{ data.startDate }} ~
              {{ data.endDate }}
            </div>
            <div class="text-xs mb-2">
              <span class="font-bold">신청기간:</span> ~ {{ data.deadlineDate }}
              <span class="text-red-500 font-bold">({{data.applicationPeriod}}일 후 마감)</span>
            </div>
            <div class="text-xs">
              <span class="font-bold">모집인원:</span> {{ data.applicantCount }}명
              / {{ data.applicantMaxCount }}명
            </div>
          </div>
          <div class="flex flex-row px-3 mt-2 pb-2">
            <span
              v-for="(item, index) in data.keywords"
              :key="index"
              class="
                inline-block
                bg-gray-200
                rounded-full
                px-2
                py-1
                text-xs
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
    </div>
  </a>
</template>

<style scoped>
  #title {
   overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;
  }

  #description {
   overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 2; /* number of lines to show */
   -webkit-box-orient: vertical;
  }
</style>

<script lang="ts">
import { reactive, ref, onMounted, computed } from "vue";
import moment from "moment";

export default {
  props: {
    item: {
      type: Object as any,
      required: true,
    },
  },
  setup({ item }) {
    const data = computed(() => {
      return {
        ...item,
        startDate: moment(item.startDate.toDate()).format("YYYY-MM-DD"),
        endDate: moment(item.endDate.toDate()).format("YYYY-MM-DD"),
        deadlineDate: moment(item.deadlineDate.toDate()).format("YYYY-MM-DD"),
        applicationPeriod: moment(item.deadlineDate.toDate()).diff(
          moment(),
          "days"
        ),
      };
    });

    return { data };
  },
};
</script>
