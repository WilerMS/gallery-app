import { DeleteIcon } from '@app/icons'
import { type Image as ImageType } from '@app/types'
import { Image } from '@nextui-org/react'
import { type FC } from 'react'

interface Props extends ImageType {
}

const Figure: FC<Props> = ({ title, url, likes, liked }) => {
  return (
    <div className="relative group w-full flex rounded-2xl overflow-hidden mb-5 min-h-[300px] max-h-[400px] md:max-h-[600px]">
      <Image
        className="w-full h-full object-cover z-0"
        alt={title}
        src={url}
        loading='lazy'
      />
      <button className="absolute group-hover:opacity-100 transition-all opacity-0 top-2 right-2 rounded-full bg-white w-[30px] h-[30px] flex items-center justify-center shadow-lg">
        <DeleteIcon />
      </button>
      <div className="absolute shadow-top group-hover:bottom-0 -bottom-full bg-[#00000076] transition-all w-full text-white px-[10px] pb-10 pt-2">
        <h2 className="text-xl">{title}</h2>
      </div>
    </div>
  )
}

export default Figure
