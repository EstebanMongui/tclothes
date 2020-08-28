"""Pictures clothes."""

# Django
from django.db import models

# Utils
from tclothes.utils.baseModels import TClothesModel


class ClothesPictureModel(TClothesModel):
    """Model for pictures clothe."""
    clothe = models.ForeignKey(
        'clothes.ClothesModel',
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        'Picture image',
        upload_to='clothes/pictures/',
    )

    def __str__(self):
        """Return id picture and clothe str representation."""
        return f'{self.image.url}'