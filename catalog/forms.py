from django.core.exceptions import ValidationError

from django import forms
from django.forms import BooleanField, BaseInlineFormSet

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner")

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in words:
            if word in cleaned_data:
                raise ValidationError(f"Слово {word} не может содержаться в названии")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in words:
            if word in cleaned_data:
                raise ValidationError(f"Слово {word} не может содержаться в описании")
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("is_published", "description", "category")


class VersionForm(StyleFormMixin, forms.ModelForm):
    """ VersionForm"""

    class Meta:
        model = Version
        fields = "__all__"


class VersionFormSet(BaseInlineFormSet):
    """ Проверка между формами"""
    def clean(self):
        super().clean()
        active_versions = [form.cleaned_data for form in self.forms
                           if form.cleaned_data.get('is_active')]
                           # and not form.cleaned_data.get('DELETE', False)]
        if len(active_versions) > 1:
            raise ValidationError("Может быть только одна активная форма")

        return active_versions
