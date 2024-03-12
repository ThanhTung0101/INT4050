from django.views.generic import TemplateView

from app.models import Post


class HomePage(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        posts = Post.objects.order_by("-date_published")
        NUMBER_OUTSTANDING_NEWS = 6
        featured_news_list = posts[:NUMBER_OUTSTANDING_NEWS]

        context["page_name"] = "home"
        context["featured_news_list"] = featured_news_list
        return self.render_to_response(context)
