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

from views import DetailNewsPage, HomePage, NewsPage, WellcomePage

urlpatterns = [
    path("", include("app.urls")),
    path("api/", include("api.urls")),
    re_path(r"^admin/", admin.site.urls),
    path("", WellcomePage.as_view(), name="wellcome_page"),
    path("home/", HomePage.as_view(), name="home"),
    path("news/", NewsPage.as_view(), name="news"),
    path(
        "news/detail/<int:post_id>/",
        DetailNewsPage.as_view(),
        name="detail_news",
    ),
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
