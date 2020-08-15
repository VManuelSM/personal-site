from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Project, Technology


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'technologies': technologies})

class ProyectView(DetailView):
    model = Project
    template_name = 'portfolio/proyect_detail.html'

