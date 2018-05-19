# Entry point for flask app
import datetime
from flask import Flask
from flask_restful import Api
from api.__init__ import app
from flask_jwt import JWT, jwt_required, current_identity
from api.resources.v1.meals import Meal, MealList
from api.resources.v1.orders import Order, OrderList
from api.resources.v1.menu import Menu
from api.resources.v1.users import User
from api.resources.v1.registration import Registration
from api.resources.v1.login import Login

flask_app = app

def setup_routes():
    api = Api(flask_app) 

    api.add_resource(Registration,'/api/v1/auth/register/')
    api.add_resource(Login, '/api/v1/auth/login/')

    api.add_resource(OrderList, '/api/v1/orders/')
    api.add_resource(Order, '/api/v1/orders/<int:order_id>')

    api.add_resource(MealList, '/api/v1/meals/')
    api.add_resource(Meal, '/api/v1/meals/<int:meal_id>')

    api.add_resource(Menu, '/api/v1/menu/')
