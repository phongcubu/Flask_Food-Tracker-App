from flask import Flask
from .main.routes import main
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_food'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    db.init_app(app)

    return app