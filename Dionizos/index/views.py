from django.shortcuts import render
from index.models import Wines
from django.db.models import Q

def index(request):
    wines = None

    wines_filter = Q()
    wines = Wines.objects.filter(wines_filter)
    return render(request,
            template_name="index/index.html",
            context={"wines": wines})

def produkt(request):
    return render(request,
                  template_name="index/produkt.html")