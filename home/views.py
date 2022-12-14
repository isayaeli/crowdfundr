
import json
import math
import string
import random
import requests
from django.shortcuts import get_object_or_404, redirect, render
from home.models import Contact
from sme.models import Donation, Project, Word_of_support
from donors.models import Opportunity
from userauth.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
key = settings.API_KEY
url = "https://swahiliesapi.invict.site/Api"
headers = {'User-Agent': 'Mozilla/5.0'}



def home(request):
    projects = Project.objects.all().order_by('-id')[:3]
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
    qs = request.GET.get('q')
    if qs :
        projects = Project.objects.filter(
            Q(user=qs)|
            Q(title__icontains=qs)
        )
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
        # print(request.POST)
        order_id = ''.join(random.sample(string.ascii_lowercase, 12))
        amount =  int(request.POST['amount'])
        name =  request.POST['name']
        user = project.user
        project = project.id
        obj  = Donation(user=user, project_id=project,name=name,donation=amount,donation_id=order_id)
        obj.save()
        # print(order_id)
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
        "is_live":True,
        "success_url": "https://crowdimpact.me/",
        # "cancel_url": "https://9a00-41-222-180-250.in.ngrok.io/cancel",
        # "webhook_url": "https://9a00-41-222-180-250.in.ngrok.io/response",
        
      
     
        }}
    response = requests.post(url,  headers=headers, json=payload)
    # print(response.json())
    response = response.json()
    response = response['payment_url']
    # print(response)
    return response



from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def payment_response(request):
  
    payload = {"api":170, "code":103,"data":{
     "api_key": key
    }
    }
    response = requests.post(url,  headers=headers, json=payload)
    # print(response.json())
    response = response.json()
    # print(response)
    donation = Donation.objects.all()
    for data in response['orders']:
        for d in donation:
            if data['client_order_id'] in d.donation_id and data['status'] == "paid":
               d.verified = True
               d.save()
        

    context = {
     
    }
    return render(request, 'home/success.html', context)

@require_http_methods(['GET', 'POST'])
def payment_cancelled(request):
 
    context = {
       
    }
    return render(request, 'home/cancelled.html', context)


def word(request, id):
    if request.method == 'POST':
        word =  request.POST.get('word')
        user = request.POST['user']
        project = request.POST['project']
        obj = Word_of_support(user_id=user,project_id=project,word=word)
        obj.save()
        return redirect('donate',id=id)
        

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        response_message = {}
        contact =Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        response_message['result'] = "Successful submited"
        return HttpResponse(
            json.dumps(response_message),
            content_type = 'application/json'
        )
    return HttpResponse(
        json.dumps({"Error":'Something went Wrong'}),
        content_type = 'application/json'
    )





def fw_donate(request,id):
    project  = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        # print(request.POST)
        order_id = ''.join(random.sample(string.ascii_lowercase, 12))
        amount =  int(request.POST['amount'])
        name =  request.POST['name']
        user = project.user
        project = project.id
        obj  = Donation(user=user, project_id=project,name=name,donation=amount,donation_id=order_id)
        obj.save()
        return redirect(str(fw_process_payment(name,amount, order_id)))
    context = {
        'data':project
    }
    return render(request, 'home/donate.html', context)




def fw_process_payment(name,amount, order_id):
    auth_token= settings.RAVE_SECRET_KEY
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
            "tx_ref":order_id,
            "amount":amount,
            "currency":"TZS",
            "redirect_url":"http://localhost:5000/callback",
            "payment_options":"card, ussd",
            # "meta":{
            #     "consumer_id":customer_id,
            #     "consumer_mac":"92a3-912ba-1192a"
            # },
            "customer":{
                "email":'info@crowdimpact.me',
                "phonenumber":'255 745 831 623',
                "name":name
            },
            "customizations":{
                "title":"CrowdImpact",
                "description":"Donate to Help Startups",
                "logo":"http://localhost:5000/static/assets/img/logo.png"
            }
            }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link


from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(['GET', 'POST'])
def fw_payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    donation =  Donation.objects.filter(donation_id=tx_ref)[0]
    # print(donation.donation_id)
    if  donation.donation_id == tx_ref and  status == 'successful':
        donation.verified = True
        donation.save()

    context = {
        'status':status,
        'tx_ref':tx_ref,
    }
    return render(request, 'home/fw_response.html', context)
