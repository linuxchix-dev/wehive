from flask import Flask
from config import Config

app = Flask(__name__) 
app.config.from_object(Config)     

from app import routes     #this is to avoid circular imports

'''this __init__.py acts as the starting point of the application, Flask class
which is imported from flask, the instance of the Flask class is our WSI application
(main web app)'''
 
