from django import forms

from inflows.models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 3})
        }
        labels={
            'supplier': 'Fornecedor',
            'product': 'Product',
            'quantity': 'Quantity',
            'description': 'Descrição'
        }
