from django import forms

from .models import Review


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',
            'content'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'New review' not in title:
            raise forms.ValidationError(message='This is not a valid review title')
        return title

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if 'new review' not in content:
            raise forms.ValidationError(message='This is not valid review content')
        return content
