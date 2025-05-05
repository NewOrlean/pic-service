from abc import ABC
from backend.domain.models import ImageCloud, ImageDB


class AbstractDBRepository(ABC):
    def upload_image(self, image_cloud: ImageCloud) -> ImageDB:
        pass

    def delete_image(self, image_id: str) -> str:
        pass