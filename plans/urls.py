from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Ana sayfa → panel'e yönlendir
    path("", lambda request: redirect("dashboard"), name="home"),

    # Dashboard ve işlemler
    path("panel/", views.dashboard, name="dashboard"),
    path("create/", views.RootPlanCreateView.as_view(), name="create_rootplan"),
    path("edit/<int:pk>/", views.RootPlanUpdateView.as_view(), name="edit_rootplan"),
    path("delete/<int:pk>/", views.RootPlanDeleteView.as_view(), name="delete_rootplan"),
    path("export/", views.export_visits_excel, name="export_visits_excel"),
    path("logout/", views.logout_view, name="logout"),
]
