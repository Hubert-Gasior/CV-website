from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def exp_page(request):
    template = loader.get_template('exp_page.html')
    return HttpResponse(template.render())

def hobby_page(request):
    template = loader.get_template('hobby_page.html')
    return HttpResponse(template.render())

def qualities_page(request):
    template = loader.get_template('qualities_page.html')
    return HttpResponse(template.render())
