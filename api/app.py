# Entry point for flask app
import datetime
from flask import Flask
from flask_restful import Api
from api.__init__ import create_app
from flask_jwt import JWT, jwt_required, current_identity
from api.resources.v1.meals import Meal, MealList
from api.resources.v1.orders import Order, OrderList
from api.resources.v1.menu import Menu
from api.resources.v1.users import User
from api.resources.v1.registration import Registration
# from api.resources.v1.login import Login

app = create_app('development_env')
api = Api(app)

@app.route('/bookameal/api/v1/auth/login/')
@jwt_required()
def protected():
    return '%s' % current_identity

api.add_resource(Registration,'/bookameal/api/v1/auth/register/')
# api.add_resource(Login, '/bookameal/api/v1/auth/login/')

api.add_resource(OrderList, '/bookameal/api/v1/orders/')
api.add_resource(Order, '/bookameal/api/v1/orders/<int:order_id>')

api.add_resource(MealList, '/bookameal/api/v1/meals/')
api.add_resource(Meal, '/bookameal/api/v1/meals/<int:meal_id>')

api.add_resource(Menu, '/bookameal/api/v1/menu/')
