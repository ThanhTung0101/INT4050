from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from app.models import Comment, Forum
from libs import BaseViewMixin


class ForumDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Forum
    template_name = "pages/detail_forum.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        forum = self.get_object()
        content_type = ContentType.objects.get_for_model(Forum)
        context["comments"] = Comment.objects.filter(
            content_type=content_type,
            object_id=forum.pk,
        )
        return context
