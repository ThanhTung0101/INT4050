from .auth.login import LoginView
from .document.create import DocumentCreateView
from .document.list import DocumentListView
from .profile.detail import ProfileDetailView
from .profile.update import ProfileUpdateView

__all__ = [
    "DocumentListView",
    "LoginView",
    "ProfileDetailView",
    "ProfileUpdateView",
    "DocumentCreateView",
]
