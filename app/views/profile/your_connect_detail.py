from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Connect, ConnectTicket
from libs import BaseViewMixin


class YourConnectDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Connect
    template_name = "pages/my_request.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["accepted_tickets"] = ConnectTicket.objects.filter(
            connect=self.get_object(),
            accepted=True,
        )
        context["request_tickets"] = ConnectTicket.objects.filter(
            connect=self.get_object(),
            accepted=False,
        )
        return context
