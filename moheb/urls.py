from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path("admin/login/", views.CustomAdminLoginView.as_view(), name="admin_login"),
    path("admin/", admin.site.urls, name="admin"),
    path("", include("website.urls")),
]
