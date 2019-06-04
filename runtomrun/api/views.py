from django.shortcuts import render
from django.http import JsonResponse

from routing.routing import check

def index(request):
    return JsonResponse({'foo':f'{check(2)}'})