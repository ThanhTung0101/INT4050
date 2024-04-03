from django.urls import path

from . import views

urlpatterns = [
    path(
        "documents/", views.DocumentListView.as_view(), name="documents-list"
    ),
    path("login/", views.LoginView.as_view(), name="login"),
]
