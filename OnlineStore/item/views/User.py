from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from ..models import User


class Create(CreateView):
    model = User
    fields = "__all__"
    template_name = "user/create.html"

    def get_success_url(self):
        return reverse("user-list")


class List(ListView):
    model = User
    template_name = "user/list.html"
    context_object_name = "users"


class Detail(DetailView):
    model = User
    template_name = "user/detail.html"
    context_object_name = "user"


class Update(UpdateView):
    model = User
    fields = "__all__"
    template_name = "user/update.html"
    context_object_name = "user"

    def get_success_url(self):
        return reverse("user-detail", args=[self.object.pk])


class Delete(DeleteView):
    model = User

    def get_success_url(self):
        return reverse("user-list")
