from flask import Flask,request
from modules import model as m
from controllers import apiendpoints
from flask_swagger_ui import get_swaggerui_blueprint

#instantiate flask app, sqlalchemy db from the modules and creating the table 
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=m.db
db.init_app(app)
with app.app_context():
    db.create_all()

#calling the blueprints from the controllers
app.register_blueprint(apiendpoints.get_blueprint())
app.register_blueprint(apiendpoints.get_swagger(),url_prefix='/swagger')


