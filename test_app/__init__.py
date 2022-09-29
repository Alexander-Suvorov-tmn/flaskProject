from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_apscheduler import APScheduler

from config import Config
from .database import OrderData, sess
from .views import TestDataView


app = Flask(__name__)
app.config.from_object(Config)
ma = Marshmallow(app)
api = Api(app)

sched = APScheduler()
sched.init_app(app)
sched.start()
