from django.shortcuts import render, redirect
from index.models import Wines
from index.forms import WineForm, SearchForm
from django.db.models import Q


def index(request):

    form = SearchForm(request.POST)
    wines = None
    if form.is_valid():
        wines_filter = Q()

        if form.cleaned_data["fraze"] != "":
            wines_filter &= Q(Q(name__icontains=form.cleaned_data["fraze"])
                                |Q(color__icontains=form.cleaned_data["fraze"])
                                |Q(taste__icontains=form.cleaned_data["fraze"]))
        wines = Wines.objects.filter(wines_filter)
    return render(request,
            template_name="index/index.html",
            context={"form":form,
                    "wines": wines})


def produkt(request):
    return render(request,
                  template_name="index/produkt.html")

def dodaj(request):
    form = WineForm(label_suffix="")
    if request.POST:
        form = WineForm(request.POST,
                          label_suffix="")
        if form.is_valid():
            form.save()
            return redirect(" ")
    return render(request,
                  template_name="edytuj/edytuj.html",
                  context={"form": form})
    return render(request,
                  template_name="dodaj/dodaj.html")
def opinie(request):
    return render(request,
                  template_name="opinie/opinie.html")
