from django import forms
from userauth.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm


class oppForm(forms.Form):
    title = forms.CharField()
    image = forms.FileField( widget=forms.FileInput())
    details = forms.CharField()
    deadline =forms.DateField()





class userForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round','placeholder':'username'}), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-round','placeholder':'email'}), label='email')
   
    password = None

    class Meta:
        model = User
        fields = ('username','email')


    
class profileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-round'}),label='Profile Photo')


    class Meta:
        model = Profile
        fields = '__all__'
        exclude =('user','user_type','overview')