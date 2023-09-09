from django.urls import path
from .views import index, add_post

urlpatterns = [
    path('', index, name='index'),
    path('add', add_post, name='add_post'),
]
