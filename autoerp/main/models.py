from django.db import models

# Create your models here.

class Client(models.Model):
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


class Contact(Client):
    prenom = models.CharField(max_length=254, blank=True)
    #entreprise_employeuse = models.ForeignKey(
    #                        'Entreprise',
    #                        on_delete=models.CASCADE,
    #                        blank=True,
    #                                )

    def __str__(self):
        return (self.prenom+' '+self.nom)


class Entreprise(Client):
    siret = models.PositiveIntegerField()
    employes = models.ManyToManyField(Contact, through='Emploi')

    def __str__(self):
        return self.nom


class Emploi(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    poste = models.CharField(max_length=254, blank=True)
    
    def __str__(self):
        #if self.poste: intitule = self.contact+', '+self.poste+' chez '+self.entreprise
        #else: intitule = self.contact+' chez '+self.entreprise

        if self.poste: intitule = str(self.contact)+', '+str(self.poste)+' chez '+str(self.entreprise)
        else: intitule = str(self.contact)+' chez '+str(self.entreprise)
        return intitule

