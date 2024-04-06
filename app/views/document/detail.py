from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Document
from libs import BaseViewMixin


class DocumentDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Document
    template_name = "pages/detail_document.html"
