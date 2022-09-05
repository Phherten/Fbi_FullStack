"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, MafiaMember, Subordinate
from api.utils import generate_sitemap, APIException
import requests
import json

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200


@api.route('/add', methods=['POST', 'GET'])
def add():
    url = "https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    members = response_json["members"]
    
    for i in members:
        member = i
        mafiaMember = MafiaMember(
            name = member["name"],
            boss = member["boss"],
            seniority = member["seniority"],
            is_free = True
        )
        mafiaMember.save()
    return "todo Ok"

@api.route('/add_subordinate', methods=['POST', 'GET'])
def add_subordinate():
    url = "https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    members = response_json["members"]
    
    for i in members:
        member = i
        if member["subordinates"]:
            member_subordinates = member["subordinates"]
            for i in member_subordinates:
                subordinate = i
                subordinates = Subordinate(
                    name = member["name"],
                    subordinate = subordinate
                )
                subordinates.save()
                    
        
    return "todo Ok"


    
         

            
        

        
        
        
    



    

    


