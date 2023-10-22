import firebase_admin
from firebase_admin import credentials, auth, db

def initialize_firebase():
    cred = credentials.Certificate("ledge-exports-firebase-adminsdk-ie9ta-5bcd17ee8c.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ledge-exports-default-rtdb.firebaseio.com/"})

def sign_up(name, email, password, user_type):
    try:
        user = auth.create_user(
            email=email,
            password=password,
        )
        user_uid = user.uid

        # Store additional user information in the Realtime Database
        user_data = {
            "uid": user_uid,
            "name": name,
            "email": email,
            "user_type": user_type,
            "password": password
        }

        ref = db.reference(f"/Users/{user_uid}")
    
        ref.set(user_data)

        return user
    except Exception as e:
        return str(e)

def login(email, password):
    try:
        user = auth.get_user_by_email(email= email)
        ref = db.reference('/Users')  # Adjust the database reference path as per your database structure
        user_data = ref.child(user.uid).get()
        if(user_data["password"]== password):
            return user, user_data
        else:
            return "Password"
    except Exception as e:
        return str(e)

def get_user_data(user_id):
    try:
        ref = db.reference('/Users')  # Adjust the database reference path as per your database structure
        user_data = ref.child(user_id).get()
        return user_data
    except Exception as e:
        print(f"Error: {e}")
        return None


