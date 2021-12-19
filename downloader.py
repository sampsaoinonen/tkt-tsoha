import csv
from db import db

def get_data(file_name, hidden, user_id):

    with open("uploads/" + file_name) as stats:                #here data from already downloaded csv-file                 
        try:
            db.session.execute("INSERT INTO Files (file_name, hidden, user_id) VALUES (:file_name, :hidden, :user_id)", {"file_name":file_name, "hidden":hidden, "user_id":user_id})        
            db.session.commit()
            
            result = db.session.execute("SELECT id FROM Files WHERE file_name=:file_name AND user_id=:user_id", {"file_name":file_name, "user_id":user_id})
            file_id = result.fetchone()[0]        
            
            for row in csv.reader(stats, delimiter=","):    #is being parsed into sql-table        
                if row[0] == "\ufeff" or row[0] == "Player Name":
                    continue
                
                sql =  "INSERT INTO players (name, team, pos, games, goals, assists, points, plusminus, penalty, shots, gwg, ppg, ppa, shg, sha, hits, blocked, file_id) VALUES (:name, :team , :pos, :games, :goals, :assists, :points, :plusminus, :penalty, :shots, :gwg, :ppg, :ppa, :shg, :sha, :hits, :blocked, :file_id)"
                to_insert = {"name":row[0], "team":row[1], "pos":row[2], "games":row[3], "goals":row[4], "assists":row[5], "points":row[6], "plusminus":row[7],  
                "penalty": row[8], "shots":row[9], "gwg":row[10], "ppg":row[11], "ppa":row[12], "shg":row[13], "sha":row[14], "hits":row[15], "blocked":row[16], "file_id":file_id}
                db.session.execute(sql, to_insert)
        except:
            print("jeeeeeee")
            return False
    db.session.commit()
    return True

def user_id_and_filename_used(file_name, user_id):    
    result = db.session.execute("SELECT count(*) FROM files WHERE file_name=:file_name AND user_id=:user_id", {"file_name":file_name, "user_id":user_id})
    if result.fetchone()[0] > 0:        
        return True
    return False

def get_filenames_and_ids(user_id):
    result = db.session.execute("SELECT id, file_name FROM files WHERE user_id=:user_id OR hidden=:hidden" , {"user_id":user_id, "hidden":"f"}).fetchall()    
    return result

def get_fileids(user_id):
    result = db.session.execute("SELECT id FROM files WHERE user_id=:user_id OR hidden=:hidden" , {"user_id":user_id, "hidden":"f"}).fetchall()
    fileids = []
    for r in result:        
        stripped = str(r).replace(",", "").replace("('", "").replace("')", "")        
        fileids.append(stripped)        
    return fileids
    