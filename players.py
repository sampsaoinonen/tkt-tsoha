from db import db
import downloader


def get_column_names():
    columns = db.session.execute("SELECT column_name FROM information_schema.columns WHERE table_name='players' ORDER BY ordinal_position")
    result = columns.fetchall()  ## tästä muuttujien nimiä korjattava
    columns = []
    for r in result:        
        stripped = str(r).replace(",", "").replace("('", "").replace("')", "")        
        columns.append(stripped)
    return columns

def get_all():
    result = db.session.execute("SELECT * FROM players")
    return result.fetchall()
    
def get_player(id): ## tarviiko olla file_id ollenkaan?
    result = db.session.execute("SELECT * FROM players WHERE id=:id", {"id":id})
    #result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id AND id=:id", {"file_id":file_id, "id":id})
    return result.fetchone()

def get_players(file_id):
    result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id", {"file_id":file_id})
    return result.fetchall()


def organize_players(organize, file_id):                       
    if is_column_type_text(organize):
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize, {"file_id":file_id})
    else:
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize + " DESC", {"file_id":file_id})
    return result.fetchall()

def organize_players_reverse(organize_reverse, file_id):                       
    if is_column_type_text(organize_reverse):
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize_reverse + " DESC", {"file_id":file_id})
    else:
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize_reverse, {"file_id":file_id})
    return result.fetchall()

def is_column_type_text(column): # gives boolean is column type text or not
    result = db.session.execute("SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'players' AND COLUMN_NAME = '" + column + "'")
    return str(result.fetchone()[0]) == "text"

def get_likes(id):
    result = db.session.execute("SELECT count(L.likes) FROM Players P, Playerlikes L WHERE L.player_id=:id AND L.player_id=P.id", {"id":id})
    likes = result.fetchone()
    return likes
    

