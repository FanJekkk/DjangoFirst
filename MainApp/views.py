from django.shortcuts import render, HttpResponse

name = "Иван"
surname = "Иванов"

def about(request):
    info = f"<h1><i>Автор: {name} {surname}</i></h1>"
    return HttpResponse(info)

def home(request):
    return HttpResponse("Hello")
