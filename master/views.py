from django.shortcuts import render

from tutorials.models import TutorialSeries

def home(request):
    series = TutorialSeries.objects.filter(archived=False).order_by('-id')[:3]
    template = 'home.html'
    context ={'series': series}
    return render(request, template, context)
