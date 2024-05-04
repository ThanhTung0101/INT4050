from django.views.generic import ListView

from app.models import Document, Subject


class DocumentListView(ListView):
    model = Document
    template_name = "pages/documents.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        subjects = self.request.GET.get("subjects")
        if subjects:
            queryset.filter(subjects__in=[subjects])

        return queryset
