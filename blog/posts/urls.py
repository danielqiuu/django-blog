from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:st>', views.post, name='post')

]