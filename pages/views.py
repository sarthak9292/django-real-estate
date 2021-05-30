from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from sellers.models import Seller
from listings.choices import state_choices, price_choices, bedroom_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html',context)

def about(request):
    sellers = Seller.objects.order_by('-hire_date')

    mvp_sellers = Seller.objects.all().filter(is_mvp=True)

    context = {
        'sellers': sellers,
        'mvp_sellers': mvp_sellers
    }
    return render(request, 'pages/about.html',context)