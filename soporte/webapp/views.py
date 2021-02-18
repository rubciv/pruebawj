
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
    import requests

    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"dropdown": "italy"}

    headers = {
        'x-rapidapi-key': "cb5a72895amshfe4c9b910ff10eep137693jsnf0f1a383cda0",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

