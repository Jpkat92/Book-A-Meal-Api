# Entry point for flask app
import datetime
from flask import Flask, render_template, make_response
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Resource
from resources.v1.meals import MealResource, MealListResource
from resources.v1.orders import OrderResource, OrderListResource
from resources.v1.menu import MenuResource
from resources.v1.registration import RegistrationResource
from resources.v1.login import LoginResource
from resources.v1.default import DefaultResource

class ApiInstance(object):
    
    def __init__(self, api_instance):
        self.api = api_instance

    def setup_routes(self):
        self.api.add_resource(DefaultResource, '/')

        self.api.add_resource(RegistrationResource,'/api/v1/auth/register/')

        self.api.add_resource(OrderListResource, '/api/v1/orders/')
        self.api.add_resource(OrderResource, '/api/v1/orders/<int:order_id>')

        self.api.add_resource(MealListResource, '/api/v1/meals/')
        self.api.add_resource(MealResource, '/api/v1/meals/<int:meal_id>')

        self.api.add_resource(MenuResource, '/api/v1/menu/')


