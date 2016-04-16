from django.contrib import admin

from .models import Contact, People, Company, Job

# Register your models here.

class JobInline(admin.TabularInline):
    model = Job
    extra = 0


class PeopleAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': (('first_name', 'name'))}),
            ('Adresse Postale',{
                'classes': ('collapse', ),
                'fields': (('address_1', 'address_2', ), ('zipcode', 'city'))
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
    inlines = [JobInline]
    pass


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': (('name', 'siret'), )}),
            ('Adresse Postale',{
                'classes': ('collapse', ),
                'fields': (('address_1', 'address_2', ), ('zipcode', 'city'), )
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
    inlines = [JobInline]
    pass


admin.site.register(People, PeopleAdmin)
admin.site.register(Company, CompanyAdmin)
