from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "main_app/index.html")


