from django.views.generic import TemplateView


class WellcomePage(TemplateView):
    template_name = "pages/wellcome_page.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "wellcome_page"
        return self.render_to_response(context)
