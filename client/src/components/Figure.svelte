<script>
  export let url
  export let label
</script>


<div class="relative group w-full rounded-xl overflow-hidden float-left mb-[10px] md:mb-[30px] max-h-[400px] md:max-h-[600px]">
  <img
    class="w-full h-full object-cover"
    src="{url}"
    alt="{label}"
  />
  <button class="absolute group-hover:opacity-100 transition-all opacity-0 z-40 top-2 right-2 rounded-full bg-white w-[30px] h-[30px] flex items-center justify-center shadow-lg">
    <iconify-icon icon="uil:trash" class="text-xl m-0 text-red-700"></iconify-icon>
  </button>
  <div class="absolute shadow-top group-hover:bottom-0 -bottom-full bg-[#00000076] transition-all w-full text-white px-[10px] pb-10 pt-2">
    <h2 class="text-xl">{label}</h2>
  </div>
</div>