from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from . import views

urlpatterns = [
    path('token/verify/messages', views.get_messages),
    path('message/<str:id>', views.get_message),
    path('token/verify/message_create', views.create_message),
    path('token/verify/login', views.login)

]