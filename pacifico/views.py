from django.shortcuts import render
from django.views.generic import ListView

class IndexView(ListView):
    def acceso_home(request):
        template = 'home.html'
        return render(request, template)

