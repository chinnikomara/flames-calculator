from . import views
from django.urls import path
urlpatterns=[
    path('',views.show),
    path('result',views.res,name="result"),
]