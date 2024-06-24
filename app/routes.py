from flask import Flask # From the flask module import Flask class

app = Flask(__name__)   # Create an instrance of the Flask class (an object)

#Obejct Orienting Paradigm (OOP), things are represented as classes. 
@app.get("/")           # Flask decorator that helps us create routes
def about():
    me = {              # this is a dictionary 
        "first_name": "Kevin",
        "last_name": "Cabrera",
        "hobbies": "DIY stuff and watching TV",
        "is_online": True
    }
    return me            # Flask will convert compatible dictionareis into JSON for us!

