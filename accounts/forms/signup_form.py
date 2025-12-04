from django import forms
from django.core.exceptions import ValidationError
from ..services.validators import (
    validate_username,
    validate_full_name,
    validate_age,
    validate_phone_number,
    validate_email_address,
    validate_password,
    validate_confirm_password,
    validate_agree_to_terms,
)

class SignupForm(forms.Form):
    """
    Form representing the Monash sign-up fields.

    Validation is delegated to functions in accounts.services.validators
    to keep the logic modular and easy to read.
    """
    username = forms.CharField(
        label="Username",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    age = forms.IntegerField(
        label="Age",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    phone_number = forms.CharField(
        label="Phone Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    email = forms.CharField(
        label="Email Address",
        max_length=100,
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    password = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    agree_to_terms = forms.BooleanField(
        label="I agree to the terms",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    # Field-level clean methods calling our validator functions

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return validate_username(username)

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return validate_full_name(full_name)

    def clean_age(self):
        age = self.cleaned_data.get("age")
        # age is already an int here (IntegerField), but we still check range
        return validate_age(age)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        return validate_phone_number(phone_number)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return validate_email_address(email)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return validate_password(password)

    def clean(self):
        """
        Form-wide validation that depends on multiple fields.
        """
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        agree_to_terms = cleaned_data.get("agree_to_terms")

        # Confirm password must match, if both were provided
        if password is not None and confirm_password is not None:
            try:
                validate_confirm_password(password, confirm_password)
            except ValidationError as e:
                self.add_error("confirm_password", e)

        # "Agree to terms" must be checked
        try:
            validate_agree_to_terms(agree_to_terms)
        except ValidationError as e:
            self.add_error("agree_to_terms", e)

        return cleaned_data
