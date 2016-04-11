from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact, Personne, Entreprise, Emploi

# Create your views here.

@login_required
def index(request):
    contacts = Contact.objects.all()
    return render(
                request, 
                'contact/index.html', 
                {
                    'contacts' : contacts,
                }
            )


@login_required
def entreprise_index(request):
    contacts = Entreprise.objects.all()

    return render(
                request, 
                'contact/index.html', 
                {
                    'contacts' : contacts,
                }
            )


@login_required
def personne_index(request):
    contacts = Personne.objects.all()

    return render(
                request, 
                'contact/index.html', 
                {
                    'contacts' : contacts,
                    #'personnes' : personnes,
                }
            )
