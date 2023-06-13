from django import forms

class Register(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=30)
    last_name = forms.CharField(label="Last Name",max_length=20)
    username = forms.CharField(label="Username",max_length=20)
    email = forms.EmailField(label="Email")
    passowrd = forms.CharField(label="Password",widget=forms.PasswordInput)



