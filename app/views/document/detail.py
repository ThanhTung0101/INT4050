from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from app.models import Comment, Document
from libs import BaseViewMixin


class DocumentDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Document
    template_name = "pages/detail_document.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        document = self.get_object()
        content_type = ContentType.objects.get_for_model(Document)
        context["comments"] = Comment.objects.filter(
            content_type=content_type,
            object_id=document.pk,
        )
        return context
