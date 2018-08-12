from django.shortcuts import render


def index(request):
    return render(request, 'guestbookapp/index.html')


def sign(request):
    return render(request, 'guestbookapp/sign.html')
