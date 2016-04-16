from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, People, Company, Job
from main.views import pagerDict

# Create your views here.



@login_required
def index(request,page=1,itemsByPage=5):
    firstItem = (int(page) - 1) * int(itemsByPage)
    print('firstItem : '+str(firstItem)) # DEBUG
    lastItem = int(firstItem + int(itemsByPage))
    print('lastItem : '+str(lastItem)) # DEBUG
    contacts = Contact.objects.all()[firstItem:lastItem]
    context = {
            'contacts' : contacts, 
            'pager':     pagerDict(Contact, page, itemsByPage, 'contact:index'),   
            }
    return render(request, 'contact/index.html', context)


@login_required
def company_index(request):
    contacts = Company.objects.all()

    return render(request, 'contact/index.html', {'contacts' : contacts, })


@login_required
def company_view(request, item_id):
    #contacts = Company.objects.get(id=company_id)
    contact = get_object_or_404(Company, id=item_id)

    return render(request, 'contact/view.html', {'contact' : contact, })


@login_required
def company_edit(request, company_id):
    #contacts = Company.objects.get(id=company_id)
    contact = get_object_or_404(Company, id=company_id)

    return render(request, 'contact/company_form.html', {'company' : company, })


@login_required
def people_index(request):
    contacts = People.objects.all()

    return render(request, 'contact/index.html', {'contacts' : contacts, })


@login_required
def people_view(request, people_id):
    people = People.objects.get(id=people_id)

    return render(request, 'contact/index.html', {'people' : people, })


