from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.


class Contact(PolymorphicModel):
    nom = models.CharField(max_length=254)
    adresse1 = models.CharField(max_length=254, blank=True)
    adresse2 = models.CharField(max_length=254, blank=True)
    code_postal = models.CharField(max_length=254, blank=True)
    ville = models.CharField(max_length=254, blank=True)
    telephone = models.CharField(max_length=254, blank=True)
    telephone_mobile = models.CharField(max_length=254, blank=True)
    telephone_pro = models.CharField(max_length=25, blank=True)
    fax = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True)
    note = models.TextField(blank=True)
    website = models.URLField(blank=True)


class People(Contact):
    prenom = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return (self.prenom+' '+self.nom)

    def isPeople(self):
        return True


class Company(Contact):
    siret = models.PositiveIntegerField()
    raison_sociale = models.CharField(max_length=254)
    employes = models.ManyToManyField(People, through='Emploi')

    def __str__(self):
        return self.nom

    def isCompany(self):
        return True



class Emploi(models.Model):
    personne = models.ForeignKey(People, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Company, on_delete=models.CASCADE)
    poste = models.CharField(max_length=254, blank=True)
    
    def __str__(self):
        #if self.poste: intitule = self.contact+', '+self.poste+' chez '+self.entreprise
        #else: intitule = self.contact+' chez '+self.entreprise

        if self.poste: intitule = str(self.personne)+', '+str(self.poste)+' chez '+str(self.entreprise)
        else: intitule = str(self.personne)+' chez '+str(self.entreprise)
        return intitule

