from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('images/<str:image_type>/', views.get_images, name='get_images'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.couple_detail, name='couple_detail'),
]
