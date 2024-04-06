from django.urls import path

from . import views

urlpatterns = [
    path(
        "documents/", views.DocumentListView.as_view(), name="documents-list"
    ),
    path(
        "documents/contribute/",
        views.DocumentCreateView.as_view(),
        name="document-create",
    ),
    path(
        "documents/detail/<int:pk>/",
        views.DocumentDetailView.as_view(),
        name="document-detail",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileDetailView.as_view(), name="profile"),
    path(
        "profile/update/",
        views.ProfileUpdateView.as_view(),
        name="profile-update",
    ),
]
