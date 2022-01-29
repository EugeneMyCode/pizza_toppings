from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    """"Пицца, созданная пользователем"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        """"Возвращает строковое представление модели"""
        return self.name

class Topping(models.Model):
    """"Топпинги для конкретной пиццы"""
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"Возвращает строковое представление модели"""
        return self.name