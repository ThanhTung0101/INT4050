from .auth.login import LoginView
from .document.create import DocumentCreateView
from .document.detail import DocumentDetailView
from .document.list import DocumentListView
from .profile.detail import ProfileDetailView
from .profile.update import ProfileUpdateView

__all__ = [
    "DocumentListView",
    "LoginView",
    "ProfileDetailView",
    "ProfileUpdateView",
    "DocumentCreateView",
    "DocumentDetailView",
]
