from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/')


class Hashtag(models.Model):
    title = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None, null=True)

    '''hashtags'''
    hashtags = models.ManyToManyField(Hashtag)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    def __str__(self):
        return f"Отзыв для продукта '{self.product.name}'"

