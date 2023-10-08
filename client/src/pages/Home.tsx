import Figure from '@app/components/Figure'
import FloatingActionButton from '@app/components/FloatingActionButton'
import { useImages } from '@app/hooks/useImages'
import cn from 'classnames'
import InfiniteScroll from 'react-infinite-scroll-component'

export default function Home () {
  const { images, hasNextPage, totalImages, fetchNextPage } = useImages()

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
        dataLength={totalImages}
        next={fetchNextPage}
        hasMore={hasNextPage}
        loader={<></>}
      >
        {images.map(({ images }) => (
          images.map(image => <Figure key={image._id.$oid} {...image} />)
        ))}
      </InfiniteScroll>

      <FloatingActionButton />

    </main>
  )
}
