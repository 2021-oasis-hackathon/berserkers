import { computed, onMounted, onUnmounted, ref } from "vue"

export default function () {
  let windowWidth = ref(window.innerWidth)

  const onWidthChange = () => windowWidth.value = window.innerWidth
  onMounted(() => window.addEventListener('resize', onWidthChange))
  onUnmounted(() => window.removeEventListener('resize', onWidthChange))
  
  const type = computed(() => {
    if (windowWidth.value < 768) return 'xs'
    if (windowWidth.value >= 768 && windowWidth.value < 1025) return 'sm'
    if (windowWidth.value >= 1025 && windowWidth.value < 1280) return 'md'
    if (windowWidth.value >= 1280) return 'lg'
  })

  const width = computed(() => windowWidth.value)

  return { width, type }
}
