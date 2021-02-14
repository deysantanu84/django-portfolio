from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    myContext = {
        'title': 'this is about us',
        'my_number': 123,
        'my_bool': True,
        'my_list': [123, 456, 789, 'abc'],
        'my_html': '<h1>Hello World</h1>'
    }
    return render(request, "about.html", myContext)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")
