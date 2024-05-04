from django.views.generic import ListView

from app.models import Forum


class ForumListView(ListView):
    model = Forum
    template_name = "pages/forum.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
