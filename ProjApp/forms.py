from django import forms
from .models import Source
from ProjAppAuth.models import CustomPermission


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control'})


class UploadForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"
        exclude = ["username", "total_rating_count", "total_ratings",
                   "created_at", "updated_at", "total_hits", "ratings"]


class CustomPermissionForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = CustomPermission
        fields = "__all__"
