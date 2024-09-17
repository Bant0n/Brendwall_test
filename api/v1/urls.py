from django.urls import path

from .products import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('products/', views.ProductView.as_view()),
]
