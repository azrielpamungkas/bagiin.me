from django.test import TestCase

from shorten.forms import ShortenForm


# Create your tests here.
class ShortenTestCase(TestCase):
    def test_form(self):
        f = ShortenForm()
        data = {
            'title': 'Dokumen siswa',
            'slug': 'dokumen-2022',
            'url': 'www.google.com'
        }
        f = ShortenForm(data)
        if f.is_valid():
            print(f.cleaned_data['title'])
            f.save()
        else:
            print(f.errors.as_data())
