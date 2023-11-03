from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('messages', views.get_messages),
    path('message/<str:id>', views.get_message),
    path('message_create', views.create_message),
    path('message/update/<str:id>', views.update_Message),
    path('message/delete/<str:id>', views.delete_Message),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]