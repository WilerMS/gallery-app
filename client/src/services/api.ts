export function api<T> (url: URL | string, options: RequestInit = {}): Promise<T> {
  // Get Authorization Bearer from local storage.
  const token = localStorage.getItem('AuthorizationBearer')
  const headers = token
    ? { ...options.headers, Authorization: `Bearer ${token}` }
    : options.headers

  return fetch(url, { ...options, headers })
    .then(response => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json() as Promise<T>
    })
}
