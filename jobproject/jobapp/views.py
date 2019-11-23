from django.shortcuts import render
from jobapp.models import hydjob,kerjob,banjob,chejob
from django.http import HttpResponse
from . import forms

# Create your views here.
def index(request):
    return render(request, 'jobapp/home.html')
def home(request):
    return render(request, 'jobapp/base.html')
# Create your views here.
def banjobview(request):
    job_list = banjob.objects.all()
    my_dict={'job_list': job_list}
    return render (request, 'jobapp/banjobs.html', context = my_dict)
def kerjobview(request):
    kjob_list = kerjob.objects.all()
    my_dict={'kjob_list': kjob_list}
    return render (request, 'jobapp/kerjobs.html', context = my_dict)
def chejobview(request):
    cjob_list = banjob.objects.all()
    my_dict={'cjob_list': cjob_list}
    return render (request, 'jobapp/Chejobs.html', context = my_dict)
def hydjobview(request):
    hjob_list = hydjob.objects.all()
    my_dict={'hjob_list': hjob_list}
    return render (request, 'jobapp/hydjobs.html', context = my_dict)
def hydform(request):
    form=forms.hydjobregister
    if request.method=='POST':
        form=forms.hydjobregister(request.POST)
        if form.is_valid():
            form.save()
        return hydjobview(request)
    return render(request,'jobapp/register.html', {'form':form})

def kerform(request):
    form=forms.kerjobregister
    if request.method=='POST':
        form=forms.kerjobregister(request.POST)
        if form.is_valid():
            form.save()
        return kerjobview(request)
    return render(request,'jobapp/register.html', {'form':form})
