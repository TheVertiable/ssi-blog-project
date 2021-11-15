from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    home_html = "<h1> Wlcome to Home Page </h1>"
    return HttpResponse(home_html)


def about(request):
    about_html = "<h1> Wlcome to About Page </h1>"
    return HttpResponse(about_html)

