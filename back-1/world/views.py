from django.shortcuts import render
from django.http import HttpResponse

def HelloUser(request):
    return HttpResponse("Hello user")