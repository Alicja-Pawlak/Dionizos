from django.shortcuts import render

def dodaj(request):
    return render(request,
                  template_name="dodaj/dodaj.html")