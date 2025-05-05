import  logging

from backend.domain.models import ImageFront
from backend.repositories.cloudinary_repository import CloudinaryRepository
from backend.repositories.db_repository import DBRepository


logger = logging.getLogger(__name__)


class UploadImage:
    def __init__(self,
                 cloudinary_repository: CloudinaryRepository,
                 db_repository: DBRepository):
        self.cloudinary_repository = cloudinary_repository
        self.db_repository = db_repository

    def execute(self, image_front: ImageFront):
        image_cloud = self.cloudinary_repository.upload_image(image_front)
        logger.info('Сompleted successfully: Image added to Cloudinary')
        image_db = self.db_repository.upload_image(image_cloud)
        logger.info('Сompleted successfully: Image added to DB')
        return image_db