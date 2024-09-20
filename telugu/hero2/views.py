from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    return HttpResponse("Bade bade deshon mein aisi choti choti baatein hoti rehti hain, Senorita")
def func2(request):
    return HttpResponse("Kabhi kabhi jeetne ke liye kuch haarna padta hai. Aur haar ke jeetne waale ko Baazigar kehte hai.")