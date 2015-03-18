from flask import Flask
app = Flask(__name__)

# define our models
class User(Model):
    user_id = UUID(primary_key=True)
    name = Text()
    email = Text(required=True)

class EmailToUser(Model):
    email = Text(primary_key=True)
    user_id = UUID(required=True)

class LoginHistory(Model):
    # TTL = 60 days
    user_id = UUID(primary_key=True)
    login_date = DateTime(primary_true=True)
    ip_address = Text()
    
# routes

@app.before_first_request
def connect_to_db():
    print "Connecting to cassandra"
    try:
        setup(["localhost"], "users_demo")
    except Exception as e:
        print e

# routes


print("Starting up the demo app")
app.run(port=7777)

