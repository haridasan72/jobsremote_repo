from django import forms
from jobapp.models import hydjob , kerjob
class hydjobregister(forms.ModelForm):
    class Meta:
        model = hydjob
        fields = '__all__'
class kerjobregister(forms.ModelForm):
    class Meta:
        model = kerjob
        fields = '__all__'
