from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Item(models.Model):
    item = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="item/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.item
