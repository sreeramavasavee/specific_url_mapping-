from django.urls import path
from app1.views import*
app1_name='anything'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('first1/',first1,name='first1')
]