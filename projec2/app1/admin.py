from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Category, Comment, Company, Product, ProductSite, ProductSize,Image
# Register your models here
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('pk','name','content')
    list_filter = ('category',)

#admin.site.register(Product, ProductAdmin) <- admin.site.register method

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Company)
#admin.site.register(Product)
admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Image)




#admin.site.site_header = “Product Review Admin”
