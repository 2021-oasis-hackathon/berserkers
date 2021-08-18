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
            src="https://images.unsplash.com/photo-1567619435005-4d3be491538d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8OTB8fG11cmFsfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
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
          벽에 따뜻한 마음을 그려요
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
          개인 프로그램 기획
        </div>
        <div class="mb-2 text-blueGray-600 mt-4">
          낙후된 지역에 벽화를 그려서 아름답게 <br />
          재탄생시키는 봉사 모임입니다.<br />
          그림 못 그리는 분도 환영
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
                10명
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
                30명
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
                D-46
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
          신청하기 - 신청 시 이메일로 연락
        </button>
      </div>
      <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
        <div class="flex flex-wrap justify-center">
          <div class="w-full">
            <p class="mb-4 text-md leading-relaxed text-blueGray-700">
              저와 함께 10월 1일부터 10월 30일까지 20일정도 마을에서 머물면서
              벽화도 그리고, 마을에 계신 분들과 이런저런 얘기도 하면서 지낼
              25분을 구합니다! 아무래도 그림을 그리는 일이다 보니까, 미대 분들을
              주로 받고 싶어요. 다만 그 외에도 할 일은 많으니 (페인트 통 나르기,
              밑색 깔기… 등) 그림을 못 그리는 분들도 많은 관심 부탁해요!
              감사합니다.
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
      window.location.href = "/personal-programs";
    };

    return {
      onSubmitApplication,
    };
  },
};
</script>
