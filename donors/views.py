from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Opportunity
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    opps = Opportunity.objects.filter(user=request.user).order_by('-id')
    context = {
        'opps':opps
    }
    return render(request, 'donors/donor.html',context)


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
    return render(request, 'donors/opps.html', context)

def add_opportunity(request):
    if request.method == 'POST':
        print(request.POST)
        opportunity = Opportunity()
        form = oppForm(request.POST, request.FILES)
        if form.is_valid():
            opportunity.user=request.user
            opportunity.title = form.cleaned_data['title']
            opportunity.image = form.cleaned_data['image']
            opportunity.details = form.cleaned_data['details']
            opportunity.deadline = form.cleaned_data['deadline']
            opportunity.save()
            return redirect('donor')
        else:
            messages.error(request,'An error occured while submitting a form')
            return redirect('donor')


def update_opportunity(request,id):
    opportunity = get_object_or_404(Opportunity, id=id)
    if request.method == 'POST':
        opportunity.user = request.user
        opportunity.title = request.POST['title']
        if 'image' in request.FILES:
            opportunity.image = request.FILES['image']
        opportunity.details = request.POST['details']
        opportunity.deadline = request.POST['deadline']
        opportunity.save()
        return redirect('donor')


def delete_opportunity(request,id):
    opportunity = get_object_or_404(Opportunity, id=id)
    opportunity.delete()
    messages.success(request, 'successfull deleted an opportinity')
    return redirect('donor')



def donor_profile(request):
    if request.method == 'POST':
       
        uform = userForm(request.POST, instance=request.user)
        pform = profileForm(request.POST, request.FILES, instance=request.user.profile)
      
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
           
            messages.success(request, f"Succesful updated profile")
            return redirect('profile')
    else:
        uform = userForm(instance=request.user)
        pform = profileForm(instance=request.user.profile)
     
    context = {
        'pform':pform,
        'uform':uform,
       
    }
    return render(request, 'donors/profile.html', context)

@login_required(login_url='/login')
def donors(request):
    donors = Profile.objects.filter(user_type='donor')
    context  = {
        'donors':donors
    }
    return render(request, 'donors/donors.html', context)