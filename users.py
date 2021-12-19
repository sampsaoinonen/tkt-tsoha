from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def get_liked(player_id, user_id): 
    result = db.session.execute("SELECT likes FROM PlayerLikes WHERE player_id=:player_id AND user_id=:user_id", {"player_id":player_id, "user_id":user_id})
    return result.fetchone()
       
def set_liked(player_id, user_id):
    if get_liked(player_id, user_id):
        db.session.execute("DELETE FROM Playerlikes WHERE player_id=:player_id AND user_id=:user_id", {"player_id":player_id, "user_id":user_id})
        db.session.commit()
    
    else:
        db.session.execute("INSERT INTO Playerlikes (likes, player_id, user_id) VALUES (:likes, :player_id, :user_id)", {"likes":"f", "player_id":player_id, "user_id":user_id})
        db.session.commit()
