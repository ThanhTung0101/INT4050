from django.views.generic import TemplateView


class ForumPage(TemplateView):
    # cai nay nen dung listview
    template_name = "pages/forum.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # TODO: add get post in forum

        # posts = Post.objects.order_by("-date_published").prefetch_related(
        #     "translations"
        # )

        PAGE_SIZE = 8
        # paginator = Paginator(posts, PAGE_SIZE)

        current_forum_page_number = request.GET.get("page", 1)
        try:
            current_forum_page_number = int(current_forum_page_number)
        except ValueError:
            print("Error: 'page' is not an integer")
            current_forum_page_number = 1

        # forum_paginator = paginator.get_page(current_forum_page_number)

        current_page_index = []
        for index in range(PAGE_SIZE):
            current_page_index.append(
                (current_forum_page_number - 1) * PAGE_SIZE + index + 1
            )

        context["page_name"] = "forum"
        context["current_page_index"] = "current_page_index"
        return self.render_to_response(context)
