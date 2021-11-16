from django.shortcuts import get_object_or_404, reverse
from django.views.generic import CreateView, DetailView, FormView, ListView

from images.forms import ImageResizeForm, ImageUploadForm
from images.models import Images
from images.utils import resize_image


class ImageListView(ListView):
    model = Images
    context_object_name = "images"
    template_name = "index.html"


class ImageDetailView(DetailView):
    model = Images
    context_object_name = "image"
    template_name = "image_detail.html"


class ImageCreateView(CreateView):
    form_class = ImageUploadForm
    template_name = "upload.html"

    def get_success_url(self):
        return reverse("index")


class ImageResizeView(FormView):
    form_class = ImageResizeForm
    template_name = "resize.html"

    def get_success_url(self):
        return reverse("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = get_object_or_404(Images, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        resized_image = form.save(commit=False)

        image = get_object_or_404(Images, pk=self.kwargs["pk"])
        width = form.cleaned_data.get("width")
        height = form.cleaned_data.get("height")
        new_image_file, image_name = resize_image(image, width, height)

        resized_image.parent_picture = image
        resized_image.width = width
        resized_image.height = height
        resized_image.picture = new_image_file
        resized_image.name = image_name
        resized_image.save()
        return super().form_valid(form)
