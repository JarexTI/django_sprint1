from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request: HttpRequest) -> HttpResponse:
    template: str = 'pages/rules.html'
    return render(request, template)
