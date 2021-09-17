from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, Category, Company, ProductSite, ProductSize, Comment, Image
from django.contrib.auth.models import User

from versatileimagefield.serializers import VersatileImageFieldSerializer


class CompanySerializer(FlexFieldsModelSerializer):
    model = Company
    fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'products': ('app1.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('app1.CategorySerializer', {'many': True}),
            'sites': ('app1.ProductSiteSerializer', {'many': True}),
            'comments': ('app1.CommentSerializer', {'many': True}),
             'image': ('app1.ImageSerializer', {'many': True})
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'app1.CategorySerializer',
            'productsize': 'app1.ProductSizeSerializer',
            'company': 'app1.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'app1.CategorySerializer',
            'user': 'app1.UserSerializer'
        }


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
       
        sizes='product_headshot'
        # sizes=[
        #     ('full_size', 'url'),
        #     ('thumbnail', 'thumbnail__100x100'),
        # ]
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']
