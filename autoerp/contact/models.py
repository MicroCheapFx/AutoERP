from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.


class Contact(PolymorphicModel):
    name = models.CharField(max_length=254)
    address_1 = models.CharField(max_length=254, blank=True)
    address_2 = models.CharField(max_length=254, blank=True)
    zipcode = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254, blank=True)
    telephone = models.CharField(max_length=254, blank=True)
    telephone_mobile = models.CharField(max_length=254, blank=True)
    telephone_pro = models.CharField(max_length=25, blank=True)
    fax = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    note = models.TextField(blank=True)


class People(Contact):
    first_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return (self.first_name+' '+self.name)

    def isPeople(self):
        return True


class Company(Contact):
    siret = models.PositiveIntegerField()
    raison_sociale = models.CharField(max_length=254)
    peoples = models.ManyToManyField(People, through='Job')

    def __str__(self):
        return self.name

    def isCompany(self):
        return True



class Job(models.Model):
    peoples = models.ForeignKey(People, on_delete=models.CASCADE)
    companies = models.ForeignKey(Company, on_delete=models.CASCADE)
    situation = models.CharField(max_length=254, blank=True)
    
    def __str__(self):
        #if self.situation: intitule = self.contact+', '+self.situation+' chez '+self.company
        #else: intitule = self.contact+' chez '+self.company

        if self.situation: intitule = str(self.peoples)+', '+str(self.situation)+' chez '+str(self.companies)
        else: intitule = str(self.peoples)+' chez '+str(self.companies)
        return intitule

