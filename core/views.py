from django.shortcuts import render



def home(request):
	return render(request, "core/home.html")

def about(request):
	return render(request, "core/about.html")

def store(request):
	return render(request, "core/store.html")


