from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    return HttpResponse("Flute jinka mundu oodu, simham mundu kadu.")
def func2(request):
    return HttpResponse("okadu naaku edurochina vaadike risku...nenu okadiki eduru vellina vadike risku..")