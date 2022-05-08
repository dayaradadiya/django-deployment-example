from django.urls import path, include
from basicapp import views

#TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('base/',views.base,name='base'),

]
