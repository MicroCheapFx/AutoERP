from django.contrib import admin

from .models import Client, Contact, Entreprise, Emploi

# Register your models here.

class EmploiInline(admin.TabularInline):
    model = Emploi
    extra = 0


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': (('prenom', 'nom'))}),
            ('Adresse Postale',{
                'classes': ('collapse', ),
                'fields': (('adresse1', 'adresse2', ), ('code_postal', 'ville'))
                }),
            ('Téléphone / Fax',{
                'classes': ('collapse', ),
                'fields': (('telephone', 'telephone_pro', ), ('telephone_mobile', 'fax'))
                }),
            ('Internet',{
                'classes': ('collapse', ),
                'fields': (('email', 'website', ))
                }),
            (None, {
                'classes': ('collapse', ),
                'fields': (('note', )),
                }),
            ]
    inlines = [EmploiInline]
    pass


class EntrepriseAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': (('nom', 'siret'), )}),
            ('Adresse Postale',{
                'classes': ('collapse', ),
                'fields': (('adresse1', 'adresse2', ), ('code_postal', 'ville'), )
                }),
            ('Téléphone / Fax',{
                'classes': ('collapse', ),
                'fields': (('telephone', 'telephone_pro', ), ('telephone_mobile', 'fax'), )
                }),
            ('Internet',{
                'classes': ('collapse', ),
                'fields': (('email', 'website', ), )
                }),
            (None, {
                'classes': ('collapse', ),
                'fields': (('note', )),
                }),
            ]
    inlines = [EmploiInline]
    pass


#admin.site.register(Contact)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Entreprise, EntrepriseAdmin)
