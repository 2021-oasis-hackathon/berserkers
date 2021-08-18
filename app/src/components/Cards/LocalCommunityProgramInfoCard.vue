<template>
  <div
    class="
      relative
      flex flex-col
      min-w-0
      break-words
      bg-white
      w-full
      mb-6
      shadow-2xl
      rounded-lg
      mt-16
    "
  >
    <div class="px-6">
      <div class="flex flex-wrap justify-center">
        <div class="w-full flex justify-center">
          <img
            alt="..."
            src="https://images.unsplash.com/photo-1501366062246-723b4d3e4eb6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=180"
            class="w-full rounded-md shadow-xl"
            height="200px"
          />
        </div>
      </div>
      <div class="text-center mt-12">
        <h3
          class="
            text-xl
            font-semibold
            leading-normal
            mb-2
            text-blueGray-700
          "
        >
          예술, 오 비엔날레
        </h3>
        <div
          class="
            text-sm
            leading-normal
            mt-0
            mb-2
            text-blueGray-400
            font-bold
            uppercase
          "
        >
          <i class="fas fa-map-marker-alt text-md text-blueGray-400"></i>
          광주 광역시 북구
        </div>
        <div class="mb-2 text-blueGray-600 mt-4">
          디자인을 좋아하는 사람들과 작업실 공유,<br />
          스터디 조직 및 전시 관람을 해보세요!
        </div>
      </div>
      <div class="flex flex-wrap justify-center">
        <div class="w-full px-4 text-center mt-2">
          <div class="flex justify-center py-4 lg:pt-4 pt-8">
            <div class="mr-4 p-3 text-center">
              <span
                class="
                  text-xl
                  font-bold
                  block
                  uppercase
                  tracking-wide
                  text-blueGray-600
                "
              >
                4명
              </span>
              <span class="text-sm text-blueGray-400">신청인원</span>
            </div>
            <div class="mr-4 p-3 text-center">
              <span
                class="
                  text-xl
                  font-bold
                  block
                  uppercase
                  tracking-wide
                  text-blueGray-600
                "
              >
                8명
              </span>
              <span class="text-sm text-blueGray-400">모집인원</span>
            </div>
            <div class="lg:mr-4 p-3 text-center">
              <span
                class="
                  text-xl
                  font-bold
                  block
                  uppercase
                  tracking-wide
                  text-blueGray-600
                "
              >
                D-21
              </span>
              <span class="text-sm text-blueGray-400">신청마감</span>
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-wrap justify-center">
        <button
          class="
            bg-emerald-500
            text-white
            active:bg-emerald-600
            font-bold
            uppercase
            text-md
            px-8
            py-2
            rounded
            shadow
            hover:shadow-md
            outline-none
            focus:outline-none
            mr-1
            ease-linear
            transition-all
            duration-150
          "
          type="button"
          @click="onSubmitApplication"
        >
          신청하기 - 일부 유료
        </button>
      </div>
      <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
        <div class="flex flex-wrap justify-center">
          <div class="w-full">
            <p class="mb-4 text-md leading-relaxed text-blueGray-700">
              도심과 멀지 않은 한적한 마을에서 나와 비슷한 사람들과 여유롭고
              낭만 가득한 한 달을 보내보고 싶지 않으신가요? 이 마을에서라면 내가
              무엇을 하든 간섭하는 사람 없이 온전히 나만의 시간을 보낼 수도
              있고, 주변 사람들과 교류하고 소통하면서 아기자기하게 시간을 보낼
              수도 있답니다. 스터디를 조직해서 같이 공부하고 작업관을 공유하면서
              시야를 넓힐 수도 있구요!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup() {
    const onSubmitApplication = (event) => {
      event.preventDefault();
      alert("신청이 완료되었습니다.");
      window.location.href = "/local-community-programs";
    }

    return {
      onSubmitApplication
    };
  }
}
</script>
