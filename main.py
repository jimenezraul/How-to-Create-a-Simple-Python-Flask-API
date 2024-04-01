from flask import Flask, jsonify
from user import User
# Import the Car class from car.py

app = Flask(__name__) # Create a Flask app

@app.route("/users")
def users():
    users = User.users # Get the list of users

    return jsonify([user.__dict__ for user in users]) # Return the list of users as JSON
    # The __dict__ attribute returns the dictionary of the object

# TODO: Create a route that returns the list of cars
# The route should be "/cars"


if __name__ == '__main__':
   app.run(host="localhost", port=8000, debug=True) # Run the app on localhost:8000 with debug mode enabled