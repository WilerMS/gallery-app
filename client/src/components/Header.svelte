<script lang="ts">
  import 'iconify-icon'
</script>

<header class="z-50 max-w-[1400px] bg-[#ffffffe2] backdrop-blur h-[100px] w-full fixed top-0 flex justify-between items-center px-[30px]">


  <div class="w-[250px] flex items-center justify-start">
    <div class="text-3xl py-2 flex items-center justify-center rounded-lg text-slate-700 font-light">
      <span>Galerie d'Eve</span>
    </div>
  </div>

  <div class="flex items-center justify-end w-[calc(100%_-_550px)] h-full">

    <div class="relative search-bar border border-slate-400 rounded-lg overflow-hidden w-full max-w-[400px] h-[42px] flex items-center px-2">
      <label for="search" class="flex">
        <iconify-icon icon="tabler:search" class="text-2xl text-slate-400"></iconify-icon>
      </label>
      <input type="text" class="w-full h-full px-3 outline-none bg-transparent" id="search" placeholder="search by name">
    </div>
    
  </div>

  <div class="user-actions w-[300px] flex items-center justify-end gap-4">

    <button class="flex items-center gap-2 mr-2 border bg-slate-700 rounded-lg px-4 py-2 text-white">
      <iconify-icon icon="uil:upload" class="text-xl mb-[2px] font-bold"></iconify-icon>
      <span>Upload an Image</span>
    </button>
    
    <button class="flex items-center ">
      <iconify-icon icon="solar:heart-broken" class="text-2xl text-slate-800 font-bold"></iconify-icon>
    </button>

    <button class="flex items-center">
      <iconify-icon icon="solar:user-linear" class="text-2xl text-slate-800 font-bold"></iconify-icon>
    </button>


  </div>
  


</header>