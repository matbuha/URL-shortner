from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import service


# Create your views here.
def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')


def index(request):
    return render(request, 'main/index.html')


def shorten_post(request):
    return shorten(request, request.POST['url'])


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)

