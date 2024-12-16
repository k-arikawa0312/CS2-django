from django.shortcuts import render
import random

# Create your views here.
weather=['Sunny','Cloudy','Rainy','Snowy']
rain_prob=['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
def index(request):
    params={}
    params['title']='3days forecast'
    params['forecasts']=random.choices(weather,k=7)
    params['rain_prob']=random.choices(rain_prob,k=7)
    return render(request, 'forecast/index.html',params)