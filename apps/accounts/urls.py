from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, SignUpView, ProfileView, AboutView, NotificationView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("about/", AboutView.as_view(), name="about"),
    path("notifications/", NotificationView.as_view(), name="notifications"),


]


