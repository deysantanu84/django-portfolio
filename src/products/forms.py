from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TimeInput(
                                attrs={
                                    'placeholder': 'Product Title'
                                }
                            ))
    email = forms.EmailField()
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'new-class-name two',
                                          'id': 'my-id-for-textarea',
                                          'placeholder': 'Product Description',
                                          'rows': 10,
                                          'columns': 20
                                      }
                                  ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'New' not in title:
            raise forms.ValidationError(message='This is not a valid title')

        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(message='This is not a valid email')

        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='',
                            widget=forms.TimeInput(
                                attrs={
                                    'placeholder': 'Product Title'
                                }
                            ))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'new-class-name two',
                                          'id': 'my-id-for-textarea',
                                          'placeholder': 'Product Description',
                                          'rows': 10,
                                          'columns': 20
                                      }
                                  ))
    price = forms.DecimalField(initial=199.99)
