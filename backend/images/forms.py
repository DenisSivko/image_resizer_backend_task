from django import forms

from images.models import Images
from images.url_validators import check_correctness_url
from images.utils import get_image_from_url


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ("name", "url", "picture")
        labels = {
            "name": "Имя изображения",
            "url": "Ссылка",
            "picture": "Изображение",
        }

    def clean(self):
        url = self.cleaned_data.get("url")
        picture = self.cleaned_data.get("picture")
        if not url and not picture:
            raise forms.ValidationError(
                "Воспользуйтесь одним из полей для загрузки изображения!"
            )
        if url and picture:
            raise forms.ValidationError(
                "Нельзя загружать изображение "
                "одновременно из двух источников!"
            )
        if url:
            picture = get_image_from_url(url)
            self.cleaned_data["picture"] = picture
        return self.cleaned_data

    def clean_url(self):
        url = self.cleaned_data.get("url")
        check_correctness_url(url)
        return url


class ImageResizeForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ("width", "height")
        labels = {
            "width": "Ширина",
            "height": "Высота",
        }

    def clean(self):
        width = self.cleaned_data.get("width")
        height = self.cleaned_data.get("height")
        if not width and not height:
            raise forms.ValidationError(
                "Воспользуйтесь одним из полей!"
            )
        return self.cleaned_data
