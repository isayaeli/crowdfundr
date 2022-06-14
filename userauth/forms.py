from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, PasswordChangeForm


class registerForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name', 'class':'txt-input'}), required=True, label='Username')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'txt-input'}),required=True, label='Email')
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'txt-input'}),required=True, label='Password')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'txt-input'}),required=True, label='Password')


	class Meta:
		model = User
		fields = ('username','email','password1','password2')

		def save(self, commit=True):
			user = super(registerForm, self).save(commit=False)
			user = self.cleaned_data['email']
			if commit:
				user.save()
			return user
		
	



class ChangePassword(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old Password','class':'txt-input'}),required=True)
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New Password','class':'txt-input'}),required=True)
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm New Password','class':'txt-input'}),required=True)