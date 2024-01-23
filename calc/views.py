from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")




def add(request):
    fname = request.POST['firstname']
    lname = request.POST['lastname']
    return render(request, 'result.html', {'result': f'{fname} {lname}'})
