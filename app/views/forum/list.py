from django.views.generic import ListView

from app.models import Category, Forum, Tag


class ForumListView(ListView):
    model = Forum
    template_name = "pages/forum.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context
