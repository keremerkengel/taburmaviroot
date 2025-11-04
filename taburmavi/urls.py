from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from plans.views import signup_view

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", signup_view, name="signup"),

    # App
    path("", include("plans.urls")),
]
