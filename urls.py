"""FINAL-INT4050 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from views import (
    AddForumPage,
    CoupleFriendPage,
    DetailDocumentPage,
    DetailForumPage,
    DetailNewsPage,
    DocumentPage,
    ForumPage,
    HomePage,
    NewsPage,
    ProfilePage,
    SendRequestPage,
    SignIn,
    SignUp,
    UploadDocumentPage,
    WellcomePage,
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("", WellcomePage.as_view(), name="wellcome_page"),
    path("dang-nhap/", SignIn.as_view(), name="login"),
    path("dang-ky/", SignUp.as_view(), name="register"),
    path("trang-chu/", HomePage.as_view(), name="home"),
    path("doi-ban/", CoupleFriendPage.as_view(), name="couple_friends"),
    path("gui-yeu-cau/", SendRequestPage.as_view(), name="send_request"),
    path("cung-tien/", DocumentPage.as_view(), name="documents"),
    path(
        "dong-gop-tai-lieu/",
        UploadDocumentPage.as_view(),
        name="upload_document",
    ),
    path("tai-lieu/", DetailDocumentPage.as_view(), name="detail_document"),
    path("thao-luan/", DetailForumPage.as_view(), name="detail_forum"),
    path("dien-dan/", ForumPage.as_view(), name="forum"),
    path("thao-luan/", DetailForumPage.as_view(), name="detail_forum"),
    path("them-thao-luan/", AddForumPage.as_view(), name="add_forum"),
    path("tin-tuc/", NewsPage.as_view(), name="news"),
    path(
        "chi-tiet-tin-tuc/<int:post_id>/",
        DetailNewsPage.as_view(),
        name="detail_news",
    ),
    path("ho-so/", ProfilePage.as_view(), name="profile"),
    path("cms/", include("cms.urls")),
    path("post/", include("djangocms_blog.urls")),
    path("taggit_autosuggest/", include("taggit_autosuggest.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
