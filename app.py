import model

from flask import Flask
app = Flask(__name__)
app.add_url_rule('/', 'home', model.home)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
  