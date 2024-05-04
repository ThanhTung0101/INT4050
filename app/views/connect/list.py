from django.views.generic import ListView

from app.models import Connect, ExtracurricularActivity, Subject


class ConnectListView(ListView):
    model = Connect
    template_name = "pages/couple_friends.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        context[
            "extracurricularActivities"
        ] = ExtracurricularActivity.objects.all()
        return context
