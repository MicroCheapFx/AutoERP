from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, user_logged_in, login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def pagerDict(itemClass, page, itemsByPage, pagerUrl):
    itemList = []
    for i in itemClass.objects.all():
        itemList.append(i.id)

    lastPage = int((len(itemList) -1) / int(itemsByPage)) +1
    print(len(itemList))
    

    pageList = []
    pageListWidth = 7
    for i in range(0,pageListWidth):
        n = int(page) - int(pageListWidth / 2) + i
        if n > 0 and n <= lastPage:
            pageList.append(n)

    pager = {
            'position':     page,  
            'lastPage':     lastPage,
            'itemsByPage':  itemsByPage,
            'itemClass':    itemClass,
            'pageList':     pageList,
            'pagerUrl':     pagerUrl
            }
    return pager


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

