<script>

  let texto = ''
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
    texto = data
  }

  get()

</script>

<h1>{texto}</h1>