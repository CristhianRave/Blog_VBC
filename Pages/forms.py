from django import forms
from Pages.models import Page


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = (
            'title',
            'content',
            'categories',
            'image',
        )
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }
   


