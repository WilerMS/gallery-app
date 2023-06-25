<script>

  let texto = ''
  const get = async () => {

    const API_URL = import.meta.env.VITE_SERVER_HOST
    const Url = new URL(`http://${API_URL}`)
    const res = await fetch(Url)
    const data = await res.text()

    console.log({ data })
    texto = data
  }

  get()

</script>

<h1>Response from server: {texto}</h1>