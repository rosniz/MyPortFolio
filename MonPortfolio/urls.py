from django.contrib import admin
from django.urls import path

import PortFolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PortFolio.views.index, name="index")
]
