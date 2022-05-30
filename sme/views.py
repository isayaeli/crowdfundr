from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    projects =  Project.objects.filter(user=request.user)
    context = {
        'projects':projects
    }
    return render(request, 'sme/sme.html',context)


def projects(request):
    projects =  Project.objects.filter(user=request.user)

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
    return render(request, 'sme/projects.html', context)


def add_project(request):
    if request.method == 'POST':
        print(request.POST)
        project = Project()
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            project.user = request.user
            project.title = form.cleaned_data['title']
            project.goal = form.cleaned_data['goal']
            project.project_duration = form.cleaned_data['project_duration']
            project.beneficiaries = form.cleaned_data['beneficiaries']
            project.target_area = form.cleaned_data['target_area']
            project.project_overview = form.cleaned_data['project_overview']
            project.proposal = form.cleaned_data['proposal']
            project.video = form.cleaned_data['video']
            project.project_image = form.cleaned_data['project_image']
            project.save()
            return redirect('index')
        else:
            messages.error(request,'An error occured while submitting a form')
            return redirect('index')


def update_project(request,id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.user = request.user
        project.title = request.POST['title']
        project.project_duration = request.POST['project_duration']
        project.beneficiaries =request.POST['beneficiaries']
        project.target_area = request.POST['target_area']
        project.project_overview = request.POST['project_overview']
        if 'proposal' in request.FILES:
            project.proposal = request.FILES['proposal']
        if 'video' in request.FILES:
            project.video = request.FILES['video']
        project.save()
        return redirect('index')


def delete_project(request,id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    messages.success(request, 'successfull deleted a project')
    return redirect('index')







def sme_profile(request):
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
    return render(request, 'sme/profile.html', context)



