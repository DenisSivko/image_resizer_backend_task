import sys
from io import BytesIO

import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


def get_image_from_url(url):
    response = requests.get(url, stream=True).raw
    image = Image.open(response)
    file_name = url.split("/")[-1].split(".")[0]
    file_format = image.format.lower()
    output = BytesIO()
    image.save(output, format=file_format, quality=100)
    output.seek(0)
    full_file_name = f"{file_name}.{file_format}"
    picture = InMemoryUploadedFile(
        output, "ImageField", full_file_name,
        f"image/{file_format}", sys.getsizeof(output), None
    )
    return picture


def resize_image(image, width, height):
    if width is None:
        width = image.width
        image_name = f"{image.name}_0_{height}"
    elif height is None:
        height = image.height
        image_name = f"{image.name}_{width}_0"
    else:
        image_name = f"{image.name}_{width}_{height}"
    source_image = Image.open(image.picture)
    output = BytesIO()
    image_format = source_image.format.lower()
    new_image_size = (width, height)
    resized_image = source_image.resize(new_image_size)
    resized_image.save(output, format=image_format, quality=100)
    output.seek(0)
    new_image_file = InMemoryUploadedFile(
        output, "ImageField", f"{image_name}.{image_format}",
        f"image/{image_format}", sys.getsizeof(output), None
    )
    return new_image_file, image_name
