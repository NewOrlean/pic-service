import base64
import uuid
import cloudinary
import cloudinary.uploader

from django.core.files.base import ContentFile
from backend.domain.models import ImageFront, ImageCloud
from backend.domain.interfaces.abstract_cloudinary_repository import AbstractCloudinaryRepository


class CloudinaryRepository(AbstractCloudinaryRepository):
    def upload_image(self, image_front: ImageFront) -> ImageCloud:
        if not image_front.file or ';base64,' not in image_front.file:
            raise ValueError("Invalid base64 image data")

        metadata, image_str = image_front.file.split(';base64,')
        ext = metadata.split('/')[-1]

        file_name = f"{uuid.uuid4()}.{ext}"

        image_file = ContentFile(base64.b64decode(image_str), name=file_name)

        response = cloudinary.uploader.upload(
            image_file,
            folder="Images",
            use_filename=True,
            unique_filename=False
        )

        image_cloud = ImageCloud(
            image_id=response.get("public_id"),
            image_url=response.get("secure_url"),
            description=image_front.description,
            created_at=image_front.created_at
        )
        return image_cloud

    def delete_image(self, image_id: str) -> str:
        result = cloudinary.uploader.destroy(image_id)
        message = "success" if result.get("result") == "ok" else "error"
        return message