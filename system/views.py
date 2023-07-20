from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

