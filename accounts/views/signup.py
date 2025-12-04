from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from ..forms.signup_form import SignupForm

class MonashSignupView(FormView):
    """
    Display and process the Monash sign-up form.
    """
    template_name = "accounts/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("accounts:signup_success")

    def form_valid(self, form):
        """
        Called when the form has been validated successfully.

        For this workshop:
        - We don't persist anything to a database.
        - We simply redirect to the success page.
        """
        # If we ever want to inspect the data during the workshop:
        # cleaned_data = form.cleaned_data
        # print(cleaned_data)
        return super().form_valid(form)

class SignupSuccessView(TemplateView):
    """
    Simple 'thank you' page shown after successful sign-up.
    """
    template_name = "accounts/signup_success.html"
