from django.contrib.auth.decorators import login_required
from django.urls import path

from .vw import ImIn
from .vw import Login
from .vw import Logout

obj = "session"

urlpatterns = [
    path('', login_required()(ImIn.as_view()), name=f"{obj}_imin"),
    path('entrar/', Login.as_view(), name=f"{obj}_login"),
    path('salir/', Logout.as_view(), name=f"{obj}_logout"),
]
