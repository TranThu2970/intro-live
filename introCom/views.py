from django.shortcuts import render

from .models import *
# Create your views here.
def home(request):
    fields = Field.objects.filter(active=True)
    tops = TopBuilding.objects.filter(display_stt=True)[0:3]
    news = News.objects.all()[0:4]

    context = {'fields':fields, 'tops':tops, 'news':news}
    return render(request, 'introCom/index.html', context)


def about(request):

    context = {}
    return render(request, 'introCom/about.html', context)


def team(request):
    teams = Team.objects.all()

    context = {'teams':teams}
    return render(request, 'introCom/team.html', context)


def project(request):
    tops = TopBuilding.objects.filter(display_stt=True)[0:5]
    context = {'tops':tops}
    return render(request, 'introCom/project.html', context)


def field(request):
    fields = Field.objects.filter(active=True)
    context = {'fields':fields}
    return render(request,'introCom/field.html', context)


def fieldDetail(request,slug):
    fields = Field.objects.exclude(slug=slug)
    detail = Field.objects.get(slug=slug)

    context = {'detail':detail, 'fields':fields}
    return render(request,'introCom/blog-single.html', context)

def contact(request):

    context = {}
    return render(request, 'introCom/contact.html', context)