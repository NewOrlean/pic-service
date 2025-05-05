from dataclasses import dataclass
from datetime import datetime
from django.db import models


class ImageDB(models.Model):
    image_id = models.CharField(max_length=255, primary_key=True)
    image_url = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'images'
        app_label = 'domain'


@dataclass
class ImageFront:
    file: str
    description: str
    created_at: datetime


@dataclass
class ImageCloud:
    image_id: str
    image_url: str
    description: str
    created_at: datetime



