# For api/ URLS
from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'users^$', views.UserCreate.as_view(), name='account-create'),
]