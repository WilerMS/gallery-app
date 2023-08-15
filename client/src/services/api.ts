export function api<T> (url: URL | string, options: RequestInit = {}): Promise<T> {
  // TODO: Get Authorization Bearer from local storage. if undefined then do not send it
  return fetch(url, { ...options })
    .then(response => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json() as Promise<T>
    })
}
