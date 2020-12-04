from django.shortcuts import render
from django.contrib.auth.models import User

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
            else:
                return render(request, 'registration/registration.html', {
                    'error_message': "This username is already exist",
                })
        else:
            return render(request, 'registration/registration.html', {
                'error_message': "This email is already exist",
            })
    return render(request, 'registration/registration.html', {})
# Create your views here.
