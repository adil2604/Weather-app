from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
from django.http import HttpResponseRedirect
def show_weather(request):
    apikey='0418dffa5345018b72826c8e193cbfc2'
    url= "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+apikey
    info_cities={}
    form=CityForm()

    if request.method=='POST':
        req=request.POST.copy()
        form=CityForm(req)

        if form.is_valid():
            form.save()
            form=CityForm()
            return HttpResponseRedirect('/')

    cities = City.objects.all()
    d_cities = []
    time_url='http://api.timezonedb.com/v2.1/get-time-zone?key=H6KS355XNTG4&format=json&by=position&{}'
    for city in cities:
        city_icon = ''
        res = requests.get(url.format(city.name)).json()
        print(res)
        if res['cod'] != '404' and city.name not in d_cities:
            city.temp = res['main']['temp']
            lon=res['coord']['lon']
            lat=res['coord']['lat']

            time=requests.get(time_url.format('lat='+str(lat)+'&lng='+str(lon))).json()
            print(time)
            city_icon = res['weather'][0]['icon']
            info_cities[city] = {
                'temp': city.temp,
                'icon': city_icon

            }
            city.save()
            d_cities.append(city.name)

        else:
            city.delete()
    return render(request, 'temp/index.html',locals())


def delete(request,id):
    city=City.objects.get(id=id)
    city.delete()
    return HttpResponseRedirect('/')

