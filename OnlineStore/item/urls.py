from django.urls import path

from .views import User, Item

urlpatterns = [
    path("users/create", User.Create.as_view(), name="user-create"),
    path("users/list", User.List.as_view(), name="user-list"),
    path("users/<int:pk>", User.Detail.as_view(), name="user-detail"),
    path("users/<int:pk>/update", User.Update.as_view(), name="user-update"),
    path("users/<int:pk>/delete", User.Delete.as_view(), name="user-delete"),

    path("item/create", Item.Create.as_view(), name="item-create"),
    path("item/list", Item.List.as_view(), name="item-list"),
    path("item/<int:pk>", Item.Detail.as_view(), name="item-detail"),
    path("item/<int:pk>/update", Item.Update.as_view(), name="item-update"),
    path("item/<int:pk>/delete", Item.Delete.as_view(), name="item-delete"),
]
