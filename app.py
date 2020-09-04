import config
import model

from flask import Flask
app = Flask(__name__)

app.add_url_rule('/', 'home', model.home)
app.add_url_rule('/hello-flask','hello_flask', model.hello_flask)
app.add_url_rule('/test','hello_flask2', model.home)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=config.PORT)

# random comment
# Faster Java deployments
# https://spring.io/blog/2018/11/08/spring-boot-in-a-container

# Dispatch Lab
# https://d2iq-education.gitbook.io/dispatch/

# Command ommited from the Dispatch lab

# dispatch gitops app create hello-world --repository=https://github.com/ericgoode/cicd-hello-world-gitops --scm-secret gitops-secret-1

  