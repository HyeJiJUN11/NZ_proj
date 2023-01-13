from django.urls import path, include
from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI
from knox import views as knox_views
urlpatterns = [
    path("hello/", HelloAPI),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/logout/", knox_views.LogoutView.as_view(), name="know-logout"),
]