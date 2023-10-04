from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) 
app.config.from_object(Config)     
db = SQLAlchemy(app)  #database instance#
migrate = Migrate(app, db) #database migration instance#

from app import routes, models     #this is to avoid circular imports

'''this __init__.py acts as the starting point of the application, Flask class
which is imported from flask, the instance of the Flask class is our WSI application
(main web app)'''
 
