export interface FetchImages {
  page: number
  limit: number
  images: Image[]
}

export interface Image {
  _id: Id
  title: string
  description: string
  url: string
  private: boolean
  userId: string
  likes: number
  isOwner: boolean
  liked: boolean
}

export interface Id {
  $oid: string
}

declare interface User {
  x: any
}
