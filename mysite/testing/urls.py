from django.contrib import admin
from django.urls import path
from . import views
app_name = 'testing'
urlpatterns = [
    path('',views.post_share),
    path('share/',views.post_share,name='post_share'),
]
