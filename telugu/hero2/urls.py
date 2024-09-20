from django.urls import path
from hero2 import views
urlpatterns=[
    path('dailogue1',views.func1),
    path('dailogue2',views.func2)
]