from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
 


app                                   = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY']              ='e8b43583c2b0625328a28448'
db                                    = SQLAlchemy(app)

app.app_context().push()


print("===Init===")
from weather import routes