from django.shortcuts import render, redirect, get_object_or_404
from index.models import Wine, Comment, WineImage
from index.forms import WineForm, SearchForm, CommentForm, ImageForm, UserCreationForm
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User


def index(request):

    form = SearchForm(request.POST)
    wines = None
    if form.is_valid():
        wines_filter = price_min = price_max = Q()
        if form.cleaned_data["fraze"] != "":
                wines_filter &= Q(Q(name__icontains=form.cleaned_data["fraze"]))

        if form.cleaned_data["color"]:
                wines_filter &= Q(color=form.cleaned_data["color"])

        if form.cleaned_data["taste"]:
                wines_filter &= Q(taste=form.cleaned_data["taste"])

        if form.cleaned_data["price_min"]:
            wines_filter = Q(price__gte=form.cleaned_data["price_min"])

        if form.cleaned_data["price_max"]:
            wines_filter = Q(price__lte=form.cleaned_data["price_max"])

        wines = Wine.objects.filter(wines_filter,)

    return render(request,
            template_name="index/index.html",
            context={"form":form,
                    "wines": wines})

def produkt(request, pk):

     wine = get_object_or_404(Wine, pk=pk)
     WineComments = wine.comments.filter()
     new_comment = None
     new_image = None
     photos = WineImage.objects.filter(wine=wine)

     if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        image_form = ImageForm(request.POST,
                                request.FILES,)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.wine = wine
            new_comment.save()
            return HttpResponseRedirect(request.path_info)

        if image_form.is_valid():
            new_image = image_form.save(commit=False)
            new_image.wine = wine
            new_image.save()
            return HttpResponseRedirect(request.path_info)

     else:
            image_form = ImageForm()
            comment_form = CommentForm()

     return render(request,
                  template_name="index/produkt.html",
                  context = {'form': comment_form,
                             'wine': get_object_or_404(Wine, pk=pk),
                             'photos': photos,
                             'images': image_form,
                             'comments': WineComments,
                             'new_comment': new_comment})

    
@login_required
def dodaj(request):
    form = WineForm(label_suffix="")
    if request.POST:
        form = WineForm(request.POST,
                        request.FILES,
                          label_suffix="")
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request,
                  template_name="edytuj/dodaj.html",
                  context={"form": form})

def edytuj(request, pk):

    wine = get_object_or_404(Wine,
                               pk=pk)
    form = WineForm(label_suffix="",
                    instance=wine)
    if request.POST:
        form = WineForm(request.POST,
                        request.FILES,
                          label_suffix="",
                          instance=wine)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request,
                  template_name="edytuj/edytuj.html",
                  context={"form": form})

def opinie(request):
    return render(request,
                  template_name="opinie/opinie.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})