from django.contrib import admin

from posts.models import Product, Hashtag, Category


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_date', 'modified_date', 'image']


admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Category)
