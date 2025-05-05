import logging

from django.core.paginator import Paginator
from backend.domain.models import ImageDB


logger = logging.getLogger(__name__)


class PaginateImages:
    def execute(self, page: int, page_size: int, search: str) -> dict:
        images = ImageDB.objects.all()

        if search:
            images = images.filter(description__icontains=search)

        images = images.order_by('-created_at').values(
            'image_id', 'image_url', 'description', 'created_at'
        )

        paginator = Paginator(images, page_size)
        page_obj = paginator.get_page(page)

        logger.info(f"Executed paginate_images with page={page}, page_size={page_size}, search='{search}'")
        logger.info(f"Total items found: {paginator.count}, Total pages: {paginator.num_pages}")

        return {
            "images": list(page_obj),
            "current_page": page_obj.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count
        }
