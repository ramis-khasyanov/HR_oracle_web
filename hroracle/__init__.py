import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

database_string = "postgresql://{user}:{password}@{host_ip}:{port}/{database}".format(user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], host_ip=os.environ['DB_HOST_IP'], port=os.environ['DB_PORT'], database = "hroracledb")

app.config["SQLALCHEMY_DATABASE_URI"] = database_string
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app, db)

from hroracle.core.views import core
app.register_blueprint(core)

