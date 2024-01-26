from django.shortcuts import render
import requests
# Create your views here.
import datetime
def index(request):
    if 'city' in request.POST:
        city_name=  request.POST['city']
    else:
        city_name=  "Ankara"

    api_key = "api_key_bilgisi"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=tr"

    r = requests.get(url=url).json()
    print(r)
    description = r["weather"][0]["description"]
    icon = r["weather"][0]["icon"]
    temp = r["main"]["temp"]
    name = r["name"]
    day = datetime.date.today()

    return render(request, "wheather/weather.html", {
        'description':description,
        'temp':temp,
        'icon':icon,
        'name':name,
        'day': day
    })