from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    print(type(request))
    template = 'pages/rules.html'
    return render(request, template)
