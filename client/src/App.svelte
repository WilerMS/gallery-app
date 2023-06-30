<script>

  import Header from './components/Header.svelte'
  import Gallery from './components/Gallery.svelte'

  let images = []
  const get = async () => {

    const API_URL = import.meta.env.VITE_SERVER_HOST
    const Url = new URL(`http://${API_URL}/images`)
    
    Url.searchParams.append('user', 'wiler')

    const res = await fetch(Url, {
      headers:  {
        'Content-type': 'application/json'
      }
    })
    const data = await res.text()

    console.log({ data })
    try {
      images = JSON.parse(data)
    } catch {
      images = []
    }
  }

  get()

</script>

<div class="w-full min-h-full flex flex-col items-center">
  <Header />
  <Gallery {images} />
</div>