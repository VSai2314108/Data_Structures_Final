from django.urls import path
from . import views

urlpatterns =[
    path('', views.getRoutes, name="routes"),
    path('api/al/<_ctry>/<_city>/<_state>/<_mfr_>/<_make>/<_type_>/',views.getOut, name="out"),
    path('api/el/<_ctry>/<_city>/<_state>/<_mfr_>/<_make>/<_type_>/',views.getOut2, name="out"),
]