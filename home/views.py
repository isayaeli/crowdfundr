
import math
import random
import requests
from django.shortcuts import get_object_or_404, redirect, render
from sme.models import Project
from donors.models import Opportunity
from userauth.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# Create your views here.
key = settings.SWAHILIES_SECRET_KEY
url = "https://swahiliesapi.invict.site/Api"
headers = {'User-Agent': 'Mozilla/5.0'}



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
        'opportunities':opps
    }
    return render(request, 'home/opportunities.html', context)



def donate(request, id):
    project  = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        print(request.POST)
        amount =  request.POST['amount1']
        order_id = ''+str(math.floor(1000000 + random.random()*9000000)),
        return redirect(str(process_payment(amount, order_id)))
    context = {
        'data':project
    }
    return render(request, 'home/donate.html', context)


def process_payment(amount, order_id):
   
    payload = {
        "api":170, "code":101,"data":{
        "api_key":key,
        "order_id": order_id,
        "amount":amount,
        "username":"CrowdImpact",
        "phone_number":"0783262616",
        "is_live":False,
        # "cancel_url": "afrogulio.co.tz/canceled"
        }}
    response = requests.post(url,  headers=headers, json=payload)
    # print(response.json())
    response = response.json()
    response = response['payment_url']
    # print(response)
    return response




