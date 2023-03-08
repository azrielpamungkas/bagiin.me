from django.contrib import messages
from django.forms import forms
from django.http import Http404
from django.shortcuts import render, redirect

from shorten.forms import ShortenForm
from shorten.models import Shorten

def page_not_found(request):
    return render(request, '404.html')

# Create your views here.
def shorten_view(request):
    if request.method == 'POST':
        form = ShortenForm(request.POST)
        if form.is_valid():
            if form.is_exists():
                messages.success(request,
                                 {'info': 'Membuat tautan anda adalah', 'share': f"bagiin.me/{form.cleaned_data['slug']}"})
                form.save()
            else:
                messages.warning(request,
                                 {'info': 'Ganti nama short link anda', 'share': ""})
    else:
        form = ShortenForm()
    return render(request, 'shorten_form.html')


def shorten_detail(request, slug):
    try:
        print(slug)
        short = Shorten.objects.get(slug=slug)
    except:
        raise Http404('tidak ditemukan')
    return redirect(short.url)
