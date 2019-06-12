from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request) :
    cont_dict = {'name':'Chetan Bhogade', 'number':100}
    return render(request, 'first_app/index.html', cont_dict)

@login_required
def special(request):
    return HttpResponse("Your are login, Nice")

@login_required
def user_logout(request) : 
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))


def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST )
        profile_form = forms.UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid() : 
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pics' in request.FILES : 
                profile.profile_pic = request.FILES['profile_pics']
            
            profile.save()

            registered = True 
        else : 
            print(user_form.errors, profile_form.errors)
    else : 
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
    
    return render(request, 'first_app/register.html', {
                                                        'user_form' : user_form, 
                                                        'profile_form' : profile_form, 
                                                        'registered' : registered
                                                        })


def user_login(request) : 

    if request.method == 'POST' : 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user : 
            if user.is_active : 
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else : 
                return HttpResponse('Account not Active')
        else : 
            print("Someone try to login and failed!")
            print(f"Username : {username} and password : {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'first_app/login.html', {})




def other(request) :
    return render(request, 'first_app/other.html')

def relative(request) :
    return render(request, 'first_app/relative_url_templates.html')

def user_details(request) : 
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpage_list}
    return render(request, 'first_app/user_details.html', context = date_dict)

def form_name_view(request) : 
    form = forms.FormName()

    if request.method == 'POST' : 
        form = forms.FormName(request.POST)

        if form.is_valid() : 
            print("Validation successful!")
            print("Name : " + form.cleaned_data['name'])
            print("Email : " + form.cleaned_data['email'])
            print("Text : " + form.cleaned_data['text'])
            
    return render(request, 'first_app/form_page.html', {'form' : form})




