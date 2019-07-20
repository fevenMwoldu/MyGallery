from django.shortcuts import render
from django.http  import HttpResponse
from . models import Image

# Create your views here.
def welcome(request):
    photos = Image.objects.all()
    return render(request, 'index.html',{"photos": photos})


# GET /search/?category=city 
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category_name = request.GET.get("category")
        photos = Image.search_by_category(category_name)
        
        if len(photos) > 0:
            return render(request, 'all-photos/search.html',{"category_name": category_name, "photos": photos})
        else:
            message = "No photos found for category " + category_name
            return render(request, 'all-photos/search.html',{"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})