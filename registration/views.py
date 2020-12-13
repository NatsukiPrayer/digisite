from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from registration.models import Profile
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

def auth(request):
    if request.method == 'POST':
        psw = request.POST['psw']
        name = request.POST['name']
        user = authenticate(username=name, password=psw)
        if user is not None:
            login(request, user)
            match_prof = Profile.objects.get(user=user)
            if match_prof.check_digi():
                return redirect('/digistash/all_digi/', request)
            else:
                return redirect( '/digistash/1/vote/', {request, 1})
        else:
            return render(request, 'registration/login.html', {
                'error_message': "Incorrect name or password",
            })
    return render(request, 'registration/login.html', {})

def registration(request):
    if request.method == 'POST':
        psw = request.POST['psw']
        email = request.POST['email']
        name = request.POST['name']
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            try:
                match = User.objects.get(username=name)
            except User.DoesNotExist:
                user = User.objects.create_user(name, email, psw)
                user.save()
                prof = Profile.create(user=user, money=999, meat=999)
                prof.save()
                return redirect( '/registration/login/', {request, 1})
            else:
                return render(request, 'registration/registration.html', {
                    'error_message': "This username is already exist",
                })
        else:
            return render(request, 'registration/registration.html', {
                'error_message': "This email is already exist",
            })
    return render(request, 'registration/registration.html', {})
def loggout(request):
    logout(request)
    return redirect( '/registration/login/', request)
# Create your views here.
