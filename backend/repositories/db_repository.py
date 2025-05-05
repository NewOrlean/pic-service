from backend.domain.models import ImageCloud, ImageDB
from backend.domain.interfaces.abstract_db_repository import AbstractDBRepository


class DBRepository(AbstractDBRepository):
    def upload_image(self, image_cloud: ImageCloud) -> ImageDB:
        image_db = ImageDB(
            image_id=image_cloud.image_id,
            image_url=image_cloud.image_url,
            description=image_cloud.description,
            created_at=image_cloud.created_at
        )

        image_db.save()

        return image_db

    def delete_image(self, image_id: str) -> str:
        deleted_count, _ = ImageDB.objects.filter(image_id=image_id).delete()
        message = "success" if deleted_count > 0 else "error"
        return message