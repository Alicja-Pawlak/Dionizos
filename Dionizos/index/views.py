from django.shortcuts import render

def index(request):
    return render(request,
                  template_name="index/index.html")
def produkt(request):
    return render(request,
                  template_name="index/produkt.html")