
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', views.register),
    path('api/auth/login/', views.login),
    path('api/auth/logout/', views.logout),
    path("api/auth/profile/<int:id>/", views.update_profile),
    path("api/auth/user/<int:id>/", views.get_profile),
]
