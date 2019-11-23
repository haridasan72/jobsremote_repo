from django.contrib import admin
from jobapp.models import hydjob,kerjob,banjob,chejob
# Register your models here.
class hydjobadmin(admin.ModelAdmin):
    list_display = ['date'   ,  'company' ,  'title'  ,   'eligibility'   ,  'address'  ,   'email' ,   'phoneno' ]
class kerjobadmin(admin.ModelAdmin):
    list_display = ['date'   ,  'company' ,  'title'  ,   'eligibility'   ,  'address'  ,   'email' ,   'phoneno']
class banjobadmin(admin.ModelAdmin):
    list_display = ['date'   ,  'company' ,  'title'  ,   'eligibility'   ,  'address'  ,   'email' ,   'phoneno' ]
class chejobadmin(admin.ModelAdmin):
    list_display = ['date'   ,  'company' ,  'title'  ,   'eligibility'   ,  'address'  ,   'email' ,   'phoneno' ]

admin.site.register(hydjob,hydjobadmin)
admin.site.register(kerjob,kerjobadmin)
admin.site.register(chejob,chejobadmin)
admin.site.register(banjob,banjobadmin)

# Register your models here.
