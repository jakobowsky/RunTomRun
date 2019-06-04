import requests
from pprint import pprint

from django.shortcuts import render
from django.http import JsonResponse

from routing.routing import check
from runtomrun.settings import TOMTOMKEY


def get_points():
    return [[(52.41074741919478, 16.950054), (52.40970004636034, 16.954188486593846), (52.40717156612542, 16.955900712704175), (52.404643229362456, 16.954188013849087), (52.40359599999999, 16.950054), (52.404643229362456, 16.945919986150916), (52.40717156612542, 16.94420728729583), (52.40970004636034, 16.945919513406157)], [(52.40717156614406, 16.955900240009008), (52.406124192681716, 16.960034392293796), (52.403595710917706, 16.961746479998908), (52.40106737260707, 16.960033919648208), (52.40002014259811, 16.955900240009008), (52.40106737260707, 16.95176656036981), (52.403595710917706, 16.950054000019108), (52.406124192681716, 16.95176608772422)], [(52.403595999999986, 16.950054), (52.40254862590976, 16.95418781807288), (52.40002014261673, 16.955899767412976), (52.39749180275852, 16.954187345526396), (52.396444572103086, 16.950054), (52.39749180275852, 16.945920654473607), (52.40002014261673, 16.944208232587027), (52.40254862590976, 16.94592018192712)], [(52.40717156614406, 16.944207759990995), (52.406124192681716, 16.948341912275783), (52.403595710917706, 16.950053999980895), (52.40106737260707, 16.948341439630195), (52.40002014259811, 16.944207759990995), (52.40106737260707, 16.940074080351796), (52.403595710917706, 16.938361520001095), (52.406124192681716, 16.940073607706207)]]

def format_points(route):
    query = ''
    for counter, point in enumerate(route, 1):
        query += f'{round(point[0], 5)},{round(point[1], 5)}'
        if counter < len(route):
            query+=':'
    #print(query)
    return query

def get_tomtom_route(query):
    request = requests.get(
        f'https://api.tomtom.com/routing/1/calculateRoute/{query}/json?avoid=unpavedRoads&travelMode=pedestrian&key={TOMTOMKEY}'
    )
    #pprint(request.json()['routes'][0]['legs'][0]['points'])
    return request.json()['routes'][0]

def get_tomtom():
    context = {}
    for counter, route in enumerate(get_points()):
        query = format_points(route)
        context[counter] = get_tomtom_route(query)
    return context
    
    # pprint(request.json()['routes'][0]['legs'][0]['points'])
    #pprint(request.json())


def index(request, x, y, radius, length):
    
    context = get_tomtom()
    json_response = {
        'route': context
    }
    return JsonResponse(json_response)
