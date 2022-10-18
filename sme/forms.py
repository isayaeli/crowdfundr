from django import forms
from django.forms import URLInput
from userauth.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm, PasswordChangeForm

class userForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round','placeholder':'username'}), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-round','placeholder':'email'}), label='email')
   
    password = None

    class Meta:
        model = User
        fields = ('username','email')


class profileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-round'}),label='Profile Photo')
    overview = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':5}))


    class Meta:
        model = Profile
        fields = '__all__'
        exclude =('user','user_type','is_active')


class projectForm(forms.Form):
    title =  forms.CharField()
    goal =  forms.CharField()
    project_duration = forms.CharField()
    beneficiaries = forms.CharField()
    target_area = forms.CharField()
    project_overview = forms.CharField()
    video = forms.URLField(widget=forms.URLInput())
    project_image = forms.FileField( widget=forms.FileInput())



