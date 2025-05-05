from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from backend.domain.models import ImageFront
from backend.repositories.cloudinary_repository import CloudinaryRepository
from backend.repositories.db_repository import DBRepository
from backend.use_cases.delete_image import DeleteImage
from backend.use_cases.paginate_images import PaginateImages
from backend.use_cases.upload_image import UploadImage


cloudinary_repository=CloudinaryRepository()
db_repository=DBRepository()


@api_view(["POST"])
def upload_image(request):
    image_front = ImageFront(
        file=request.data['image'],
        description=request.data['description'],
        created_at=request.data['created_at'],
    )

    uploaded_image=UploadImage(
        cloudinary_repository=cloudinary_repository,
        db_repository=db_repository
    ).execute(image_front)

    if not uploaded_image:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(model_to_dict(uploaded_image), status=status.HTTP_200_OK)


@api_view(["GET"])
def paginate_images(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    search = request.GET.get("search", "")

    result = PaginateImages().execute(page=page, page_size=page_size, search=search)

    if not result:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(result, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_image(request):
    image_id = request.data.get("image_id")

    deleted_message=DeleteImage(
        cloudinary_repository=cloudinary_repository,
        db_repository=db_repository
    ).execute(image_id)

    if deleted_message == "error":
        return Response({"message": deleted_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"message": deleted_message}, status=status.HTTP_200_OK)