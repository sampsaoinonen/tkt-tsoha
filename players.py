from db import db
import downloader


def get_column_names():
    columns = db.session.execute("SELECT column_name FROM information_schema.columns WHERE table_name='players' ORDER BY ordinal_position")
    result = columns.fetchall()
    columns = []
    for r in result: # so html can show column names better       
        stripped = str(r).replace(",", "").replace("('", "").replace("')", "")        
        columns.append(stripped)
    return columns

def get_all():
    result = db.session.execute("SELECT * FROM players")
    return result.fetchall()
    
def get_player(id):
    result = db.session.execute("SELECT * FROM players WHERE id=:id", {"id":id})
    return result.fetchone()

def get_players(file_id):
    result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id", {"file_id":file_id})
    return result.fetchall()

def org_players(organize, file_id):                       
    if column_type_text(organize):
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize, {"file_id":file_id})
    else:
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize + " DESC", {"file_id":file_id})
    return result.fetchall()

def org_players_reverse(organize_reverse, file_id):                       
    if column_type_text(organize_reverse):
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize_reverse + " DESC", {"file_id":file_id})
    else:
        result = db.session.execute("SELECT * FROM players WHERE file_id=:file_id ORDER BY " + organize_reverse, {"file_id":file_id})
    return result.fetchall()

def column_type_text(column): # gives boolean is column type text or not
    result = db.session.execute("SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'players' AND COLUMN_NAME = '" + column + "'")
    return str(result.fetchone()[0]) == "text"

def get_likes(id):
    result = db.session.execute("SELECT count(L.likes) FROM Players P, Playerlikes L WHERE L.player_id=:id AND L.player_id=P.id", {"id":id})
    likes = result.fetchone()
    return likes
    

