from django.http import HttpResponse
from django.shortcuts import redirect
def index(reqeust):
    return HttpResponse('ok')

