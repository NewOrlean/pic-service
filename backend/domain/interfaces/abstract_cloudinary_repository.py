from abc import ABC
from backend.domain.models import ImageFront, ImageCloud


class AbstractCloudinaryRepository(ABC):
    def upload_image(self, image_front: ImageFront) -> ImageCloud:
        pass

    def delete_image(self, image_id: str) -> str:
        pass