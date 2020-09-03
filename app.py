import model

from flask import Flask
app = Flask(__name__)
app.add_url_rule('/', 'home', model.home)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')


# Faster Java deployments
# https://spring.io/blog/2018/11/08/spring-boot-in-a-container

# Dispatch Lab
# https://d2iq-education.gitbook.io/dispatch/

# Command ommited from the Dispatch lab

# dispatch gitops app create hello-world --repository=https://github.com/ericgoode/cicd-hello-world-gitops --scm-secret gitops-secret-1

  