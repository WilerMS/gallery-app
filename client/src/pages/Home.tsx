import Figure from '@app/components/Figure'
import QuickAddMenuButton from '@app/components/QuickAddMenuButton'
import { useImages } from '@app/hooks/useImages'
import cn from 'classnames'
import InfiniteScroll from 'react-infinite-scroll-component'

export default function Home () {
  const { images, lastPage, fetchNextPage } = useImages()

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
        hasMore={!lastPage}
        loader={<></>}
      >
        {images.map(
          image => <Figure key={image._id.$oid} {...image} />
        )}
      </InfiniteScroll>

      <QuickAddMenuButton />

    </main>
  )
}
