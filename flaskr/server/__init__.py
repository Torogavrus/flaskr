import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

app_settings = os.getenv('APP_SETTINGS', 'flaskr.server.config.DevelopmentConfig')
app.config.from_object(app_settings)

print(111111111111111111, app.config['SQLALCHEMY_DATABASE_URI'])
print(222222222222222222, app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:chokolatka@localhost:3306/td2'

db = SQLAlchemy(app)