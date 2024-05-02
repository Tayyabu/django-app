from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser,BlogPost

# forms.py



# class MyForm(forms.Form):
#     name = forms.CharField(
#         label='Name',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
#     )
#     email = forms.EmailField(
#         label='Email',
#         widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
#     )
#     message = forms.CharField(
#         label='Message',
#         widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
#     )

		
class SignUpForm(UserCreationForm):
	email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
    )
	first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
    )
	last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'})
    )

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class BlogPostForm(forms.ModelForm):
	class Meta:
		model=BlogPost	
		fields=['title','content','image']
		widgets={
			'title':forms.TextInput(attrs={'class':'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'}),
			'content':forms.Textarea(attrs={'class':'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500'}),
			}

		


		

	



