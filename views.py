from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from djangocms_blog.models import Post


def home_view(request):

    return render(
        request,
        "pages/home.html",
        context={
            "page_name": "home",
        },
    )


def couple_friends_view(request):

    return render(
        request,
        "pages/couple_friends.html",
        context={
            "page_name": "couple_friends",
        },
    )


def documents_view(request):

    return render(
        request,
        "pages/documents.html",
        context={
            "page_name": "documents",
        },
    )


def forum_view(request):

    return render(
        request,
        "pages/forum.html",
        context={
            "page_name": "forum",
        },
    )


def news_view(request):
    posts = Post.objects.order_by("-date_published").prefetch_related(
        "translations"
    )

    PAGE_SIZE = 8
    paginator = Paginator(posts, PAGE_SIZE)

    current_news_page_number = request.GET.get("page", 1)
    try:
        current_news_page_number = int(current_news_page_number)
    except ValueError:
        print("Error: 'page' is not an integer")
        current_news_page_number = 1

    news_paginator = paginator.get_page(current_news_page_number)

    current_page_index = []
    for index in range(PAGE_SIZE):
        current_page_index.append(
            (current_news_page_number - 1) * PAGE_SIZE + index + 1
        )

    return render(
        request,
        "pages/news.html",
        context={
            "page_name": "news",
            "posts": posts,
            "news_paginator": news_paginator,
            "current_page_index": current_page_index,
        },
    )


def detail_news_view(request, post_id):
    posts = Post.objects.order_by("-date_published").prefetch_related(
        "translations"
    )
    post = get_object_or_404(Post, pk=post_id)

    NUMBER_RELATED_NEWS = 4
    NUMBER_NEWS_TAGS = 3

    news_tags = post.tags.all()[:NUMBER_NEWS_TAGS]
    related_news = posts.exclude(pk=post_id)[:NUMBER_RELATED_NEWS]

    return render(
        request,
        "pages/detail_news.html",
        context={
            "page_name": "detail_news",
            "post": post,
            "news_tags": news_tags,
            "related_news": related_news,
        },
    )


def profile_view(request):

    return render(
        request,
        "pages/profile.html",
        context={
            "page_name": "profile",
        },
    )
