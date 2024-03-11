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
    add_forum_view,
    couple_friends_view,
    detail_document_view,
    detail_forum_view,
    detail_news_view,
    documents_view,
    forum_view,
    home_view,
    login_view,
    news_view,
    profile_view,
    register_view,
    send_request_view,
    upload_document_view,
    wellcome_page_view,
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("", wellcome_page_view, name="wellcome_page"),
    path("dang-nhap/", login_view, name="login"),
    path("dang-ky/", register_view, name="register"),
    path("trang-chu", home_view, name="home"),
    path("doi-ban/", couple_friends_view, name="couple_friends"),
    path("gui-yeu-cau/", send_request_view, name="send_request"),
    path("cung-tien/", documents_view, name="documents"),
    path("dong-gop-tai-lieu/", upload_document_view, name="upload_document"),
    path("tai-lieu/", detail_document_view, name="detail_document"),
    path("thao-luan/", detail_forum_view, name="detail_forum"),
    path("dien-dan/", forum_view, name="forum"),
    path("thao-luan/", detail_forum_view, name="detail_forum"),
    path("them-thao-luan/", add_forum_view, name="add_forum"),
    path("tin-tuc/", news_view, name="news"),
    path(
        "chi-tiet-tin-tuc/<int:post_id>/", detail_news_view, name="detail_news"
    ),
    path("ho-so/", profile_view, name="profile"),
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
