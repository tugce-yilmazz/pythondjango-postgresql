from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def anasayfaView(request):
   if request.user.is_authenticated:
        return render(request, 'home.html', {'name' : request.user.username })
   else:
        return render(request, 'home.html', {'name' : Misafir })