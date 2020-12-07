from django.shortcuts import render

def przepisy(request):
    return render(request,
                  template_name="przepisy/przepisy.html")