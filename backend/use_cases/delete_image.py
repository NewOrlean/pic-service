import logging

from backend.repositories.cloudinary_repository import CloudinaryRepository
from backend.repositories.db_repository import DBRepository


logger = logging.getLogger(__name__)


class DeleteImage:
    def __init__(self,
                 cloudinary_repository: CloudinaryRepository,
                 db_repository: DBRepository):
        self.cloudinary_repository = cloudinary_repository
        self.db_repository = db_repository

    def execute(self, image_id: str):
        message_cloud = self.cloudinary_repository.delete_image(image_id)
        logger.info('Сompleted successfully: Image deleted from Cloudinary')
        self.db_repository.delete_image(image_id)
        logger.info('Сompleted successfully: Image deleted from DB')
        return message_cloud