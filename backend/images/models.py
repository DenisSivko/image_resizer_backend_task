from django.db import models
from PIL import Image


class Images(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name="Имя")
    url = models.URLField(blank=True, verbose_name="Ссылка")
    picture = models.ImageField(
        blank=True, verbose_name="Изображение"
    )
    width = models.PositiveIntegerField(blank=True, verbose_name="Ширина")
    height = models.PositiveIntegerField(blank=True, verbose_name="Высота")
    parent_picture = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True,
        verbose_name="Родительское изображение", related_name="parents"
    )

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.picture.name
        self.width, self.height = Image.open(self.picture).size
        super(Images, self).save()

    class Meta:
        ordering = ["pk"]
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.name
