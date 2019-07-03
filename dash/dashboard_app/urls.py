from django.urls import path
from . import views


urlpatterns = [
    path('',views.app_page_main,name='app_page_main')
]