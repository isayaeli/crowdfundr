from django.shortcuts import render
from sme.models import Project
from donors.models import Opportunity
from userauth.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-id')[:4]
    opportunities = Opportunity.objects.all().order_by('-id')[:4]
    sme = Profile.objects.filter(user_type = 'sme').count()
    donor = Profile.objects.filter(user_type = 'donor').count()
    context = {
        'projects':projects,
        'opportunities':opportunities,
        "sme":sme,
        'donor':donor
    }
    return render(request, 'home/home.html',context)



def projects(request):
    projects = Project.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(projects, 10)
    try:
        projs = paginator.page(page)
    except PageNotAnInteger:
        projs = paginator.page(1)
    except EmptyPage:
        projs =paginator.page(paginator.num_pages)
    
    context = {
        'projects':projs
    }
    return render(request, 'home/projects.html', context)




def opportunities(request):
    opportunities = Opportunity.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(opportunities, 10)
    try:
        opps = paginator.page(page)
    except PageNotAnInteger:
        opps = paginator.page(1)
    except EmptyPage:
        opps =paginator.page(paginator.num_pages)

    context = {
        'opps':opps
    }
    return render(request, 'home/opportunities.html', context)