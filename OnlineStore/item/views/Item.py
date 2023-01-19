from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from ..models import Item


class Create(CreateView):
    model = Item
    fields = "__all__"
    template_name = "item/create.html"

    def get_success_url(self):
        return reverse("item-list")


class List(ListView):
    model = Item
    template_name = "item/list.html"
    context_object_name = "items"


class Detail(DetailView):
    model = Item
    template_name = "item/detail.html"
    context_object_name = "item"


class Update(UpdateView):
    model = Item
    fields = "__all__"
    template_name = "item/update.html"
    context_object_name = "item"

    def get_success_url(self):
        return reverse("item-detail", args=[self.object.pk])


class Delete(DeleteView):
    model = Item

    def get_success_url(self):
        return reverse("item-list")
