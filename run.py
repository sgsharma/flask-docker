#!flask/bin/python

# Import app variable from our app package
from application import app

# Invokes the run method to start the server
if __name__ == '__main__':
    app.run(port=9991, host="0.0.0.0")