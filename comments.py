from db import db
import downloader

def get_comment(id):
    result = db.session.execute("SELECT U.username, C.content, C.created_at FROM comments C, users U WHERE players_id=:id AND C.users_id=U.id ORDER BY C.id", {"id":id})
    return result.fetchall()

def add_comment(content, players_id, users_id):
    sql = "INSERT INTO comments (content, created_at, players_id, users_id) VALUES (:content, NOW(), :players_id, :users_id)"
    db.session.execute(sql, {"content":content, "players_id":players_id, "users_id":users_id})
    db.session.commit()
