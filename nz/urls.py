from nz.views import *
from django.urls import path
app_names='anything'
urlpatterns=[
    path('ravindra/',ravindra,name='ravindra'),
    path('willamson/',williamson,name='willamson')
]