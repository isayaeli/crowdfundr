from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate, logout  
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import registerForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def request_login(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successful Logged In')
            if request.user.profile.user_type == 'sme' and user.profile.is_active == True:
                return redirect('index')
            elif 'next' in request.POST:
                return redirect(request.POST.get('next'))
            elif request.user.profile.user_type == 'donor' and user.profile.is_active == True:
                return redirect('donor')
            else:
                return redirect('confirm')
        messages.error(request, 'Username or password is Incorrect!')
        return redirect('login')
        
    return render(request,  'userauth/login.html')


def register_request(request):
   
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user_type  = request.POST['user_type']
            if User.objects.filter(email=email).exists():
                messages.error(request,'User with this email already exists, Use a different email!!')
                return redirect('register')
            else:
                user = form.save()
                user.save()
                login(request, user)
                profile = Profile.objects.get(user=request.user)
                profile.user_type = user_type
                profile.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your crowdimpact account.'
                message = render_to_string('userauth/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return redirect('confirm')
                
    else:
        form = registerForm()
    context = {
        'form':form
    }
 
    return render(request, 'userauth/register.html',context )



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        # user.save()
        login(request, user)
        profile = Profile.objects.get(user=request.user)
        profile.is_active = True
        profile.save()
        return redirect('login')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return redirect('confirm-link')

def confirm_account(request):
    return render(request, 'userauth/confirm_acc.html',{})

def confirm_link(request):
    return render(request, 'userauth/confirm_link.html',{})




def logout_request(request):
    logout(request)
    messages.info(request,f"Logged out successful")
    return redirect('login')