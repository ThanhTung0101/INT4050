from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class SignUp(FormView):
    template_name = "authentication/register.html"
    # form_class = RegisterForm
    success_url = reverse_lazy("overview")

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
