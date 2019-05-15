from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Location, Category

# Create your views here.


def main_gallery(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'galleria/home.html', {"images": images, "locations": locations})


def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'galleria/search.html', {"images": searched_images, "category": search_term, "message": message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'galleria/search.html', {"message": message})
