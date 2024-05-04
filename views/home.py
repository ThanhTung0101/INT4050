from django.views.generic import TemplateView

from app.models import Document


class HomePage(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        documents = Document.objects.filter().order_by("created_at")[:6]
        context = self.get_context_data(**kwargs)

        context["documents"] = documents
        return self.render_to_response(context)
