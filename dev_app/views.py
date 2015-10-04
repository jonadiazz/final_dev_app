from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return HttpResponse("<h3>Unauthorized access.</h3>")

# Create your views here.
