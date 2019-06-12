from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

# def check_for_name(value):
#     if value[0] == value[0].lower() :
#         raise forms.ValidationError("Name Should Start With The Capital Letter!")

class UserForm(forms.ModelForm) : 
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta() : 
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta() :
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')





class FormName(forms.Form) : 
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again ")
    text = forms.CharField(widget = forms.Textarea)
    # botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self) : 
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("Gotcha Bot!!!")
    #     return botcatcher

    def clean(self) :
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail :
            raise forms.ValidationError("Email did'n Match !!!!! ")