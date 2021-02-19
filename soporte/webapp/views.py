
from django.contrib.auth import login

from django.shortcuts import redirect, render

from django.urls import reverse

from webapp.forms import CustomUserCreationForm

import requests




def dashboard(request):

    return render(request, "usuarios/dashboard.html")

def register(request):

    if request.method == "GET":

        return render(

            request, "usuarios/register.html",

            {"form": CustomUserCreationForm}

        )

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))


def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    val = request.POST.get('dropdown')
    #print(dict(countries)[val])
    #try:
     #   x = dict(countries)[val]
    #except:
     #   x= "India"
    querystring = {"country" : val}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "ea75790284mshc149cb256a0fafep18274djsn652e67f52063"
        }

    response = requests.request("GET", url, headers=headers, params = querystring).json()
    data = response['response']
    d = data[0]
    print(d)
    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered'],
        'deaths' : d['deaths']['total'],
        'new' : d['cases']['new'],
        'critical' : d['cases']['critical'],
        'tests' : d['tests']['total'],
        'day' : d['day'],
        'time' : d['time'][11:],
        'active' : d['cases']['active'],
        'new_deaths' : d['deaths']['new'],
    }


    return render(request, 'index.html', context)
