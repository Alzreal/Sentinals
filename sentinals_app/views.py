from django.shortcuts import render, redirect

def landing(request):
    return render(request, 'landing.html')

def index(request):
    return render(request, 'index.html')

def roster(request):
    return render(request, 'roster.html')

def schedule(request):
    return render(request, 'schedule.html')