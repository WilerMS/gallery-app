import Figure from '@app/components/Figure'
import { api } from '@app/services/api'
import { type Image, type FetchImages } from '@app/types'
import { useEffect, useState } from 'react'

export default function Home () {
  const [images, setImages] = useState<Image[]>([])

  useEffect(() => {
    api<FetchImages>('http://localhost:5000/api/v1/images?limit=100')
      .then((data) => {
        setImages(data.images)
        console.log(data)
      })
      .catch(() => {

      })
  }, [])

  return (
    <main className='px-6 w-full'>
      <div className="w-full h-full md:columns-8  md:gap-[30px]">
        {images.map((image) => (
          <Figure key={image._id.$oid} {...image} />
        ))}
      </div>
    </main>
  )
}
