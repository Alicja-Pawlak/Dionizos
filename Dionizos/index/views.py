from django.shortcuts import render, redirect, get_object_or_404
from index.models import Wines, Comments
from index.forms import WineForm, SearchForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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


def produkt(request, pk):
     WineFK = get_object_or_404(Wines, pk=pk)
     comments = WineFK.comments.filter()
     new_comment = None
     form = CommentForm(request.POST)

     if request.method == 'POST':
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.WineFK = WineFK
            new_comment.save()


     return render(request,
                  template_name="index/produkt.html",
                  context = {'form': form,
                             'wine': get_object_or_404(Wines, pk=pk),
                             'comments': comments,
                             'new_comment': new_comment,                            })

    

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
                  template_name="edytuj/edytuj.html",
                  context={"form": form})

    return render(request,
                  template_name="dodaj/dodaj.html",
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