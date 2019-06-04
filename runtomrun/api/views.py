from django.shortcuts import render
from django.http import JsonResponse

from routing.routing import check

def index(request, x, y, radius, length):
    json_response = {
        'routing':f'{check(2)}',
        'x': x,
        'y': y,
        'radius': radius,
        'length' :length,
    }
    return JsonResponse(json_response)