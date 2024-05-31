from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}

# Basic authentication user loader
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

# Basic Auth Protected Route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401

# JWT Protected Route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Role-based access control decorator
def role_required(role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != role:
                return jsonify({"msg": "Access forbidden: Insufficient role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

# Admin-only Route
@app.route('/admin-only', methods=['GET'])
@role_required('admin')
def admin_only():
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(debug=True)

