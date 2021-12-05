from db import db
import downloader

def get_comment(id):
    result = db.session.execute("SELECT U.username, C.content FROM comments C, users U WHERE players_id=:id AND C.users_id=U.id", {"id":id})
    return result.fetchall()

def add_comment(content, players_id, users_id):
    sql = "INSERT INTO comments (content, players_id, users_id) VALUES (:content, :players_id, :users_id)"
    db.session.execute(sql, {"content":content, "players_id":players_id, "users_id":users_id})
    db.session.commit()  