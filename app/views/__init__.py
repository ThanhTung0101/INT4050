from .auth.login import LoginView
from .connect.detail import ConnectDetailView
from .connect.list import ConnectListView
from .document.create import DocumentCreateView
from .document.detail import DocumentDetailView
from .document.list import DocumentListView
from .forum.detail import ForumDetailView
from .forum.list import ForumListView
from .post.detail import ArticleDetailView
from .post.list import ArticleListView
from .profile.detail import ProfileDetailView
from .profile.update import ProfileUpdateView

__all__ = [
    "DocumentListView",
    "LoginView",
    "ProfileDetailView",
    "ProfileUpdateView",
    "DocumentCreateView",
    "DocumentDetailView",
    "ForumListView",
    "ForumDetailView",
    "ArticleListView",
    "ArticleDetailView",
    "ConnectListView",
    "ConnectDetailView",
]
