from django import forms

from shorten.models import Shorten


class ShortenForm(forms.ModelForm):
    class Meta:
        fields = ('slug', 'url')
        model = Shorten
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'slug': forms.TextInput(attrs={'id': 'slug'})
        }

    def is_exists(self):
        slug = self.cleaned_data['slug']
        if Shorten.objects.filter(slug=slug).exists():
            return False
        return True