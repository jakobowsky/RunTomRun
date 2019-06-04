import requests
from pprint import pprint

from django.shortcuts import render
from django.http import JsonResponse

from routing.routing import generate_route
from runtomrun.settings import TOMTOMKEY


def format_points(route):
    query = ''
    for counter, point in enumerate(route, 1):
        query += f'{round(point[0], 5)},{round(point[1], 5)}'
        if counter < len(route):
            query+=':'
    #print(query)
    return query

def dict_to_arrays(points):
    #return [[obj['latitude'], obj['longitude']]for obj in points]
    query = ''
    for counter, point in enumerate(points, 1):
        query+= f"{point['latitude']},{point['longitude']}"
        if counter < len(points):
            query+=':'
    return query


def sumarize_route(route):
    points = []
    for leg in route['legs']:
        points += leg['points']
    return {
        'summary': route['summary'],
        'points': dict_to_arrays(points)
    }

def get_tomtom_route(query):
    request = requests.get(
        f'https://api.tomtom.com/routing/1/calculateRoute/{query}/json?avoid=unpavedRoads&travelMode=pedestrian&key={TOMTOMKEY}'
    )
    #pprint(request.json())
    #pprint(request.json()['routes'][0]['legs'][0]['points'])
    try:
        return request.json()['routes'][0]
    except:
        return None

def get_tomtom(x, y, length):
    context = {}
    for counter, route in enumerate(generate_route(x, y, length)):
        query = format_points(route)
        try:
            context[counter] = sumarize_route(get_tomtom_route(query))
        except:
            pass
    return context
    
    # pprint(request.json()['routes'][0]['legs'][0]['points'])
    #pprint(request.json())


# def get_best_routes(routes, length):
#     return sorted(routes, key=lambda route: abs(route['summary']['lengthInMeters']-length) )

def index(request, x, y, length):
    point_x = float(x)
    point_y = float(y)
    route_length = int(length)
    #print(point_x, point_y, route_length)
    context = get_tomtom(point_x,point_y , route_length)
    json_response = {
        #'route': get_best_routes(context, length)
        'route': context
    }
    return JsonResponse(json_response)
