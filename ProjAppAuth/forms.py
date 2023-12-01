from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm,PasswordChangeForm
from .models import User


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UserRegisterForm(StyledFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateSingleUserForm(StyledFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "userMode"]

# Add more forms in a similar way if needed



    