from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import DocumentCreateForm
from libs import BaseViewMixin


class DocumentCreateView(LoginRequiredMixin, BaseViewMixin, CreateView):
    template_name = "pages/upload_document.html"
    form_class = DocumentCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy("document-create")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Đóng góp tài liệu thành công!!!")
        return super().form_valid(form)