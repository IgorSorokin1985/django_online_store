from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name').lower()
        bad_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        for word in bad_words:
            if word in product_name:
                raise forms.ValidationError('Incorrect name of product')
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get('product_description').lower()
        bad_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        for word in bad_words:
            if word in product_description:
                raise forms.ValidationError('Incorrect name of product')
        return product_description

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["is_active"].widget.attrs['class'] = 'form-check-input'

    def clean_is_active(self):

        is_active = self.cleaned_data.get('is_active')
        all_active_versions = Version.objects.all().filter(product=self.cleaned_data.get('product')).filter(is_active=True)
        if len(all_active_versions) >= 1 and is_active:
            if len(all_active_versions.filter(number_version=self.cleaned_data.get('number_version'))) == 0:
                raise forms.ValidationError('You should choose only one active version')
            else:
                return is_active
        return is_active

    #def clean_number_version(self):
    #    current_number_version = self.cleaned_data.get('number_version')
    #    versions_with_this_number = Version.objects.all().filter(product=self.cleaned_data.get('product')).filter(number_version=current_number_version)
    #    if len(versions_with_this_number) > 1:
    #        raise forms.ValidationError('Number of version should be unify')
#
    #    return current_number_version
