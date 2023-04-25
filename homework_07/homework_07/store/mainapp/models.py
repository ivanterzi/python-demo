from django.db import models


# Create your models here.
# Магазин с техникой Apple, iphone, ipad, macbook, imac,аксы.
# Карточка - характеристика


class Accessories(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=25)
    accessories = models.ManyToManyField(Accessories)

    def __str__(self):
        return self.accessories.name


class Model(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=25)
    memory = models.CharField(max_length=10)
    generation = models.CharField(max_length=10)

    # price = models.ForeignKey(Price, on_delete=models.PROTECT)

    def __str__(self):
        return self.category.name, self.name, self.generation.name


class Card(models.Model):
    text = models.TextField(blank=True, null=True)
    model = models.OneToOneField(Model, on_delete=models.PROTECT)

    def __str__(self):
        return self.model.name

# class Price(models.Model):
#     price = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.price


# class Price(models.Model):
#     price = models.ForeignKey(Model, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.price
