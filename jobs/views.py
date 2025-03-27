from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')    

def latest_jobs(request):
    return render(request, 'jobs.html')    

def admissions(request):
    return render(request, 'admissions.html')    

def results(request):
    return render(request, 'results.html')    

def admit_cards(request):
    return render(request, 'admit-cards.html')    