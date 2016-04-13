from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact, People, Company, Emploi

# Create your views here.

@login_required
def index(request):
    contacts = Contact.objects.all()

    return render(request, 'contact/index.html', {'contacts' : contacts, })


@login_required
def company_index(request):
    contacts = Company.objects.all()

    return render(request, 'contact/index.html', {'contacts' : contacts, })


@login_required
def company_view(request, company_id):
    contacts = Company.objects.get(id=company_id)

    return render(request, 'contact/index.html', {'company' : company, })


@login_required
def people_index(request):
    contacts = People.objects.all()

    return render(request, 'contact/index.html', {'contacts' : contacts, })


@login_required
def people_view(request, people_id):
    people = People.objects.get(id=people_id)

    return render(request, 'contact/index.html', {'people' : people, })


