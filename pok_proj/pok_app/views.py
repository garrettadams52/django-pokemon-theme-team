from urllib import response
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os
import random

pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.
def index(request,poke_id = random.randrange(1,898)):
    total_poke_data = {}
    poke = f"https://pokeapi.co/api/v2/pokemon/{poke_id}" #random pokemon from index
    poke_one_responseJSON = HTTP_Client.get(poke).json() #request poke from api in json format
    total_poke_data.update({"1":poke_one_responseJSON['sprites']['front_default']}) #update data with first poke
    type_url = poke_one_responseJSON['types'][0]['type']['url'] #get type of poke
    type_responseJSON = HTTP_Client.get(type_url).json() #request type from api in json format
    num_same_type_pok = len(type_responseJSON['pokemon']) #number of pokemon of the same type
    for i in range(2,7):
        ind = random.randrange(0,num_same_type_pok) #random index for new pokemon of same type
        new_poke = type_responseJSON['pokemon'][ind]['pokemon']['url'] 
        new_poke_responseJSON = HTTP_Client.get(new_poke).json()
        total_poke_data.update({str(i):new_poke_responseJSON['sprites']['front_default']})

    #get type of random pokemon
    pp.pprint(total_poke_data)

    my_data = {
        'total_pokemon' : total_poke_data
    }

    reponse = render(request, 'pok_app/index.html', my_data)
    return reponse
