from flask import Flask, jsonify

app = Flask(__name__)

# Sample user data stored in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to serve JSON data of all usernames
@app.route('/data')
def get_usernames():
    usernames = [user['username'] for user in users.values()]
    return jsonify(usernames)

if __name__ == "__main__":
    app.run(debug=True)

# Endpoint to return status
@app.route('/status')
def get_status():
    return "OK"

# Endpoint to return user details by username
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to handle adding new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if data:
        username = data.get('username')
        if username:
            users[username] = data
            return jsonify({"message": "User added successfully", "user": data}), 201
        else:
            return jsonify({"error": "Username not provided"}), 400
    else:
        return jsonify({"error": "No data provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
