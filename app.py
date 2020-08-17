import model

from flask import Flask
app = Flask(__name__)
app.add_url_rule('/', 'home', model.home)

