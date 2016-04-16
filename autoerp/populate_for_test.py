import os
import sys
from random import randrange

sys.path.append('$HOME/srv/autoerp/autoerp')

os.environ['DJANGO_SETTINGS_MODULE'] = 'autoerp.settings'

import django
django.setup()

from contact.models import Contact, People, Company, Job
import peoplefile, companyfile

pf = peoplefile.peoples
jf = peoplefile.jobs
cf = peoplefile.companies

def recordCompany(c):
    company_to_record = Company(
            name = c[0],
            siret = c[1],
            address_1 = c[2],
            address_2 = c[3],
            zipcode = c[4],
            city = c[5],
            telephone = c[6],
            telephone_mobile = c[7],
            telephone_pro = c[8],
            fax = c[9],
            email = c[10],
            website = c[11],
            note = c[12],
            )
    company_to_record.save()

def recordPeople(c):
    people_to_record = People(
            name = c[1],
            first_name = c[0],
            address_1 = c[2],
            address_2 = c[3],
            zipcode = c[4],
            city = c[5],
            telephone = c[6],
            telephone_mobile = c[7],
            telephone_pro = c[8],
            fax = c[9],
            email = c[10],
            website = c[11],
            note = c[12],
            )
    people_to_record.save()

def recordAContact():
    contactType = randrange(0,2)
    if contactType == 1:
        l = len(cf)
        x = randrange(0, l)
        recordCompany(cf[x])
        print(cf[x])
        cf.pop(x)
    else:
        l = len(pf)
        x = randrange(0, l)
        recordPeople(pf[x])
        print(pf[x])
        pf.pop(x)

def recordAJob(p):
    cxl = []
    for co in Company.objects.all():
        cxl.append(co.id)
    cx = cxl[randrange(0,len(cxl))]  # Random in list
    c = Contact.objects.get(id=cx)
    sx = randrange(0,len(jf))
    s = jf[sx]
    job = Job.objects.create(companies=c,peoples=p,situation=s)
    job.save()
    

while (len(pf)>0 and len(cf)>0):
    recordAContact()

for p in People.objects.all():
    x = randrange(0,10)
    if x < 2:
        recordAJob(p)
        recordAJob(p)
    elif x < 8:
        recordAJob(p)
    
