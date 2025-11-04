from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.dashboard, name="dashboard"),
    path("plans/yeni/", views.RootPlanCreateView.as_view(), name="plan_create"),
    path("plans/<int:pk>/duzenle/", views.RootPlanUpdateView.as_view(), name="plan_edit"),
    path("plans/<int:pk>/sil/", views.RootPlanDeleteView.as_view(), name="plan_delete"),
    path("export-excel/", views.export_visits_excel, name="export_excel"),
    path("logout/", views.logout_view, name="logout"),
    path("create-admin/", views.create_admin, name="create_admin"),  # ✅ geçici rota
]
