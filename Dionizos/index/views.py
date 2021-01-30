from django.shortcuts import render, redirect, get_object_or_404
from index.models import Wine, Comment
from index.forms import WineForm, SearchForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def index(request):

    form = SearchForm(request.POST)
    wines = None
    if form.is_valid():
        wines_filter = Q()

        if form.cleaned_data["fraze"] != "":
            wines_filter &= Q(Q(name__icontains=form.cleaned_data["fraze"]))

        if form.cleaned_data["color"]:
                wines_filter &= Q(color=form.cleaned_data["color"])

        if form.cleaned_data["taste"]:
                wines_filter &= Q(taste=form.cleaned_data["taste"])

        wines = Wine.objects.filter(wines_filter)
    return render(request,
            template_name="index/index.html",
            context={"form":form,
                    "wines": wines})

def produkt(request, pk):

     wine = get_object_or_404(Wine, pk=pk)
     WineComments = wine.comments.filter()
     new_comment = None

     if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.wine = wine
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
     else:
         comment_form = CommentForm()


     return render(request,
                  template_name="index/produkt.html",
                  context = {'form': comment_form,
                             'wine': get_object_or_404(Wine, pk=pk),
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
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})