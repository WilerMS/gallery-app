import Figure from '@app/components/Figure'
import { useImages } from '@app/hooks/useImages'
import { AddIcon } from '@app/icons'
import cn from 'classnames'
import InfiniteScroll from 'react-infinite-scroll-component'

export default function Home () {
  const { images, fetchNextPage } = useImages()

  return (
    <main className='px-6 w-full'>
      <InfiniteScroll
        className={cn(
          'w-full h-full pb-6',
          'md:columns-4 md:gap-5',
          'lg:columns-6',
          'xl:columns-8',
          '2xl:columns-10'
        )}
        dataLength={images.length}
        next={fetchNextPage}
        hasMore={true}
        loader={<></>}
      >
        {images.map(
          image => <Figure key={image._id.$oid} {...image} />
        )}
      </InfiniteScroll>

      <button
        className={cn(
          'h-16 w-16 border-2 rounded-full center fixed bottom-6 right-6 shadow-lg bg-white',
          'dark:bg-slate-800 dark:border-gray-800'
        )}
      >
        <AddIcon width={32} height={32}/>
      </button>

    </main>
  )
}
