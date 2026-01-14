from django.shortcuts import render


def list_index(request):
    return render(request, "lists/index.html")