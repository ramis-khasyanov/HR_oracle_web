from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

from hroracle.core.views import core
app.register_blueprint(core)

