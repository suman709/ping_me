from django.http import HttpResponse


def ping_me(request):
    return HttpResponse("Hello World !!!")
