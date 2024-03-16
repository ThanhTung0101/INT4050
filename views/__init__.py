from .couple_friend import CoupleFriendPage
from .document import DetailDocumentPage, DocumentPage, UploadDocumentPage
from .forum import AddForumPage, DetailForumPage, ForumPage
from .home import HomePage
from .login import SignIn
from .news import DetailNewsPage, NewsPage
from .profile import ProfilePage, UpdateProfilePage
from .register import SignUp
from .send_request import SendRequestPage
from .wellcome import WellcomePage

__all__ = [
    "SignIn",
    "WellcomePage",
    "SignUp",
    "CoupleFriendPage",
    "HomePage",
    "ProfilePage",
    "SendRequestPage",
    "DetailNewsPage",
    "NewsPage",
    "AddForumPage",
    "DetailForumPage",
    "ForumPage",
    "DetailDocumentPage",
    "DocumentPage",
    "UploadDocumentPage",
    "UpdateProfilePage",
]
