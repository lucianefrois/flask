from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect




app = Flask(__name__)
app.config['SECRET_KEY'] = 'lfob2023lluciah'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'


db = SQLAlchemy(app)

csrf = CSRFProtect(app)
from api import routes