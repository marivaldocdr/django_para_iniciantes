from django.shortcuts import render
from django.http import HttpResponse


# Crie suas opiniões aqui.
def home_page_view(request):
    return render(request, "paginas/home.html")


def about_page_view(request):
    return render(request, "paginas/sobre.html")
