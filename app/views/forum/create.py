from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import ForumCreateForm
from libs import BaseViewMixin


class ForumCreateView(LoginRequiredMixin, BaseViewMixin, CreateView):
    template_name = "pages/add_forum.html"
    form_class = ForumCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy("forum-create")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Tạo diễn đàn thành công!!!")
        return super().form_valid(form)
