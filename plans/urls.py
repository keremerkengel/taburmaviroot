from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # 🔹 Anasayfa (root) yönlendirmesi:
    path("", lambda request: redirect("login"), name="home"),

    # 🔹 Panel ve planlama yolları:
    path("panel/", views.dashboard, name="dashboard"),
    path("plans/yeni/", views.RootPlanCreateView.as_view(), name="plan_create"),
    path("plans/<int:pk>/duzenle/", views.RootPlanUpdateView.as_view(), name="plan_edit"),
    path("plans/<int:pk>/sil/", views.RootPlanDeleteView.as_view(), name="plan_delete"),

    # 🔹 Excel dışa aktarma:
    path("export-excel/", views.export_visits_excel, name="export_excel"),

    # 🔹 Çıkış:
    path("logout/", views.logout_view, name="logout"),
]
