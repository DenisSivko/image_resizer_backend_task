from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import requests
from django.core.exceptions import ValidationError
from PIL import Image, UnidentifiedImageError

CUSTOM_URL_ERROR = ValidationError(
    "Убедитесь в правильности ссылки. "
    "URL-адрес должен иметь расширение изображения."
)


def check_correctness_url(url):
    if not url:
        return url
    try:
        urlopen(url)
    except HTTPError:
        raise CUSTOM_URL_ERROR
    except URLError:
        raise CUSTOM_URL_ERROR
    try:
        response = requests.get(url, stream=True).raw
        Image.open(response)
    except UnidentifiedImageError:
        raise CUSTOM_URL_ERROR
