from django.urls import path
from views import upload_image, paginate_images, delete_image


urlpatterns = [
    path("upload_image", upload_image),
    path("paginate_images", paginate_images),
    path("delete_image", delete_image),
]