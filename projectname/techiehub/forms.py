# forms.py
from django import forms
from .models import Feedback
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback, Reply
from django.contrib.auth.forms import UserCreationForm
from .models import Inquiry
from .models import Carpenter

class CarpenterForm(forms.ModelForm):
    class Meta:
        model = Carpenter
        fields = ['name', 'exp', 'skills', 'dob', 'address', 'number', 'completed_projects']

# forms.py
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'Door_Number']



class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'


class SignUpForm(UserCreationForm):
    # Customize fields if needed
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignUpForm(forms.Form):
    new_username = forms.CharField(label='Username', max_length=100)
    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']






class CombinedForm(UserCreationForm):
    # Add any additional fields you need for account creation here

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']





