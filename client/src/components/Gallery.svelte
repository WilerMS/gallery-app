<script>
  import Figure from './Figure.svelte'

  export let images = []
</script>

<main class="w-full mt-[120px] px-[10px] md:px-[30px] max-w-[1400px] m-auto">
  <div class="w-full h-full md:columns-4  md:gap-[30px]">
    {#each images as image}
      <Figure url={image.url} label={image.label} />
    {/each}
  </div>
</main>
