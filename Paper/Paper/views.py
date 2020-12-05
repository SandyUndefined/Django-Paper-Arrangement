from django.shortcuts import render,redirect


def json(request):
    return render(request,'json.html')