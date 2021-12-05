from db import db
import downloader

def checkTableExists():
    exists = db.session.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'players'")
    if exists.fetchone()[0] == 1:
        return True
    return False

def get_column_names():
    columns = db.session.execute("SELECT column_name FROM information_schema.columns WHERE table_name='players'")
    result = columns.fetchall()
    columns = []
    for r in result:        
        stripped = str(r).replace(",", "").replace("('", "").replace("')", "")        
        columns.append(stripped)
    return columns

def get_all():
    result = db.session.execute("SELECT * FROM players")
    return result.fetchall()
    

def get_player(id):
    result = db.session.execute("SELECT * FROM players WHERE id=:id", {"id":id})
    return result.fetchone()
    

def organize_players(organize):
    print(organize)
    result = db.session.execute("SELECT * FROM players ORDER BY length(" + organize + ") DESC, " + organize +" DESC")
    return result.fetchall()

def organize_players_reverse(organize_reverse):
    print(organize_reverse)
    result = db.session.execute("SELECT * FROM players ORDER BY length(" + organize_reverse + "), " + organize_reverse)
    return result.fetchall()