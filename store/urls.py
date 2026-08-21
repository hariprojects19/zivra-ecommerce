from django.urls import path
from .import views

urlpatterns=[
    path('',views.store,name='store'),#store main page
    path('product/<slug:product_slug>/',views.product_info,name='product-info'),#indivudual product
    path('search/<slug:category_slug>/',views.list_category,name='list-category'),#indivudual category
]