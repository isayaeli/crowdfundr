from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Opportunity
from django.contrib import messages
from .forms import *
# Create your views here.

# key = settings.SWAHILIES_SECRET_KEY
# url = "https://swahiliesapi.invict.site/Api"
# headers = {'User-Agent': 'Mozilla/5.0'}

# # Create your views here.
# class CheckoutView(View):
#     def get(self, *args, **kwargs):
#         cart = Cart.objects.get(user=self.request.user, ordered=False)
#         form = checkoutForm()
#         context={
#            'form':form,
#            'cart':cart
#         }
#         return render(self.request, 'payments/checkout.html', context)
#     def post(self,*args, **kwargs):
#         print(self.request.POST)
#         form = checkoutForm(self.request.POST or None)
#         try:
#             cart = Cart.objects.get(user=self.request.user, ordered=False)
#             if form.is_valid():
#                 address = form.cleaned_data.get('address')
#                 second_address = form.cleaned_data.get('second_address')
#                 country = form.cleaned_data.get('country')
#                 zip_code = form.cleaned_data.get('zip_code')
#                 phone = form.cleaned_data.get('phone')
#                 email = form.cleaned_data.get('email')
#                 payment = form.cleaned_data.get('payment')
#                 order_id = ''+str(math.floor(1000000 + random.random()*9000000)),
#                 order = OrderAddress(
#                     user= self.request.user,
#                     address= address,
#                     second_address= second_address,
#                     country=country,
#                     zip_code=zip_code,
#                     phone= phone,
#                     email= email,
#                     order_id = order_id

#                 )
#                 order.save()
#                 # cart.ordered = True
#                 # cart.order = order
#                 # cart.save()
#                 # send_mail(
#                 #     'New Order has been placed',
#                 #     f"Please visit your admin panel site to see order",
#                 #     'ummasoft@gmail.com',['isayaelib@gmail.com'], fail_silently=False
#                 # )
#                 if payment == 'S':
#                      return redirect('process', order_id=order_id)
#                 elif payment == 'C':
#                     return redirect('payment', payment_option='cash')
#                 else:
#                     messages.warning(self.request, "Ivalid payment method")
#             messages.info(self.request, "Failed checkout")
#             return redirect('checkout')

#         except ObjectDoesNotExist:
#             messages.error(self.request, "You do not have an active order..")
#             return redirect('cart')



# def swahilies(request, payment_option):

#     return render(request, 'payments/swahilies.html')


# def process_payment(request, order_id):
#     cart = Cart.objects.get(user=request.user, ordered=False)
#     payload = {
#         "api":170, "code":101,"data":{
#         "api_key":key,
#         "order_id": order_id,
#         "amount":cart.get_line_total,
#         "username":"Afrogulio",
#         "phone_number":"0783262616",
#         "is_live":False,
#         # "cancel_url": "afrogulio.co.tz/canceled"
#         }}
#     response = requests.post(url,  headers=headers, json=payload)
#     # print(response.json())
#     response =response.json()
#     # print(response['code'])
#     return redirect(response['payment_url'])
   

# def reconcilliation(request):
#     payload = {"api":170, "code":103,"data":{
#         "api_key":key
#         }
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     print(response.json())
#     response =response.json()
#     print(response['code'])


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


def donors(request):
    donors = Profile.objects.filter(user_type='donor')
    context  = {
        'donors':donors
    }
    return render(request, 'donors/donors.html', context)