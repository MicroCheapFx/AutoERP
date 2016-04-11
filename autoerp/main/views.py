from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, user_logged_in, login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #user_logged_in()
                #return render(request, 'main/index.html', {})
                return HttpResponseRedirect('/')
            else:
                #return render(request, 'autoerp/login.html', {})
                return HttpResponse("Votre compte est désactivé.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            #return render(request, 'autoerp/login.html', {})
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'autoerp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'autoerp/login.html', {})



@login_required
def index(request):
    return render(request, 'main/index.html', {})

