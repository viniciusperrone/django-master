from django import forms

from brands.models import Brand


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 3})
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
