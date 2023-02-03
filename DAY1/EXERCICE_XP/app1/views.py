from http.client import HTTPResponse
from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listing

# Create your views here.

def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request,'index.html',context)


def about (request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors=Realtor.objects.all().filter(is_MVP=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }

    return render(request,'about.html',context)

