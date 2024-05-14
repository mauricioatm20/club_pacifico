from django.urls import path
from pacifico.views import IndexView

urlpatterns = [
    path('', IndexView.acceso_home, name='index'),
]