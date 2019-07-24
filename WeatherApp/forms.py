from .models import City
from django.forms import ModelForm,TextInput

class CityForm(ModelForm):
    class Meta:
        model=City
        fields=['name','temp']
        widgets={'name': TextInput(attrs={'class':'form-control','placeholder':'Enter city'}),'temp': TextInput(attrs={'type':'hidden','value':'0'})}
