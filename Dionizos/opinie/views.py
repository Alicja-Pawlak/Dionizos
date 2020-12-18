from django.shortcuts import render

def opinie(request):
    return render(request,
                  template_name="opinie/opinie.html")