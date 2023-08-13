import Figure from '@app/components/Figure'
import { AddIcon } from '@app/icons'
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
      <div className="w-full h-full md:columns-4 lg:columns-10 md:gap-5">
        {images.map((image) => (
          <Figure key={image._id.$oid} {...image} />
        ))}
      </div>

      <button className='h-16 w-16 border-2 rounded-full center fixed bottom-6 right-6 shadow-lg bg-white dark:bg-slate-800 dark:border-gray-800'>
        <AddIcon width={32} height={32}/>
      </button>

    </main>
  )
}
