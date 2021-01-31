from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'New blog' not in title:
            raise forms.ValidationError(message='This is not a valid blog title')
        return title

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if 'new blog' not in content:
            raise forms.ValidationError(message='This is not a valid blog content')
        return content
