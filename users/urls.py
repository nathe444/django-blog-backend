from django.urls import path
from .views import MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView  # type: ignore

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),     # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
