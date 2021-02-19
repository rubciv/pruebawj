from django.conf.urls import include, url
from webapp.views import dashboard, register, home



urlpatterns = [
    url(r"^cuentas/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^tablero/", home, name="home"),

]
