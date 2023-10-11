import { type Children } from '@app/types'
import { Button, Modal, ModalBody, ModalContent, ModalFooter, ModalHeader, type ModalProps } from '@nextui-org/react'
import React, { type FC } from 'react'

interface _ModalProps {
  isOpen: boolean
  title: string
  className?: string
  children?: Children
  confirmButtonLabel?: string
  cancelButtonLabel?: string
  confirmButtonDisabled?: boolean
  size?: ModalProps['size']
  loading?: boolean
  errorMessage?: string
  onClose: () => void
  onCancel?: () => void
  onConfirm?: () => void
}

const _Modal: FC<_ModalProps> = ({
  isOpen,
  title,
  className = '',
  children,
  confirmButtonLabel = 'Confirm',
  cancelButtonLabel = 'Cancel',
  confirmButtonDisabled = false,
  size = 'lg',
  loading = false,
  errorMessage,
  onClose = () => { },
  onCancel,
  onConfirm
}) => {
  return (
    <Modal size={size} isOpen={isOpen} className={className}>
      <ModalContent>
        {(onModalClose) => (
          <>
            <ModalHeader className="flex flex-col gap-1">{title}</ModalHeader>
            <ModalBody>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Nullam pulvinar risus non risus hendrerit venenatis.
                Pellentesque sit amet hendrerit risus, sed porttitor quam.
              </p>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Nullam pulvinar risus non risus hendrerit venenatis.
                Pellentesque sit amet hendrerit risus, sed porttitor quam.
              </p>
              <p>
                Magna exercitation reprehenderit magna aute tempor cupidatat consequat elit
                dolor adipisicing. Mollit dolor eiusmod sunt ex incididunt cillum quis.
                Velit duis sit officia eiusmod Lorem aliqua enim laboris do dolor eiusmod.
                Et mollit incididunt nisi consectetur esse laborum eiusmod pariatur
                proident Lorem eiusmod et. Culpa deserunt nostrud ad veniam.
              </p>
              {children}
            </ModalBody>
            <ModalFooter>
              <Button color="danger" variant="light" onPress={onModalClose}>
                {cancelButtonLabel}
              </Button>
              {confirmButtonDisabled &&
                <Button color="primary" onPress={onModalClose}>
                  {confirmButtonLabel}
                </Button>
              }
            </ModalFooter>
          </>
        )}
      </ModalContent>
    </Modal>
  )
}

export default _Modal
