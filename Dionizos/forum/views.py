from django.shortcuts import render

def forum(request):
    return render(request,
                  template_name="forum/forum.html")