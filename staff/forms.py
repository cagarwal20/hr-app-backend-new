from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput, EmailInput

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']   
 
User = get_user_model()
class UserRegistrationForm(forms.Form):
    username            = forms.CharField()
    email               = forms.EmailField(widget=EmailInput)
    password1           = forms.CharField(widget=PasswordInput)
    password2           = forms.CharField(label='Confirm password', widget=PasswordInput)

    def clean_username(self):
        username        = self.cleaned_data.get('username')
        qs              = User.objects.filter(username=username)
        
        print("checking if user exists")
        if qs.exists():
            print("25")
            raise forms.ValidationError("Username is taken.")

        print("returning username")
        return username

    def clean_email(self):
        email           = self.cleaned_data.get('email')
        qs              = User.objects.filter(email=email)
        
        print("checking if email exists")
        # if qs.exists():
        #     print("25")
        #     raise forms.ValidationError("Email already exists.")

        print("returning email")
        return email


    def clean(self):
        cleaned_data    = super(UserRegistrationForm, self).clean()
        print("clean is called")
        password1        = cleaned_data.get("password1")
        password2       = cleaned_data.get("password2")
        if password1 != password2:
            print("passwords did not match")
            raise forms.ValidationError("Passwords must match.")
        
        print("returning cleaned_data")
        return cleaned_data