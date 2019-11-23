import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobproject.settings')
import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *

fake=Faker()
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager', 'TeamLead', 'Project Director', 'Construction Director'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        femail= fake.email()
        fphoneno = 8989324234283
        hydjobs_record=hydjob.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,email=femail, phoneno=fphoneno)

populate(25)
