from django.shortcuts import render
from django.http  import HttpResponse
from . models import Image

# Create your views here.
def welcome(request):
    photos = Image.objects.all()
    return render(request, 'index.html',{"photos": photos})


# GET /search/?search_term=city 
def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        photos = Image.search_by_category_or_location(search_term)
        
        if len(photos) > 0:
            return render(request, 'all-photos/search.html',{"search_term": search_term, "photos": photos})
        else:
            message = "No photos found for category or location of " + search_term
            return render(request, 'all-photos/search.html',{"message":message})

    else:
        message = "You haven't searched for any category or location."
        return render(request, 'all-photos/search.html',{"message":message})