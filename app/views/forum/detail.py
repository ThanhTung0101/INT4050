from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Forum
from libs import BaseViewMixin


class ForumDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Forum
    template_name = "pages/detail_forum.html"
