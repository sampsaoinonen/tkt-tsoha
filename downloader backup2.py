import csv
from db import db

def get_data():

    with open("nhl-stats2.csv") as stats:                #here data from already downloaded csv-file 
        for row in csv.reader(stats, delimiter=","):    #is being parsed into sql-table        
            if row[0] == "\ufeff" :
                continue
            if any("name" and "team" in r.lower() for r in row):#lets collect names for columns of table            
                print("******************************")
                print(row)
                print("___________")
                for ro in row:
                    print(ro)
                print("******************************")

                #columns = '"' + "INSERT INTO players (" + ", ".join(row) + ") VALUES (:" + ", :".join(row)  +')"'
                add_columns = '"' + "ALTER TABLE players ADD(" + " CHAR(50), ".join(row) + "CHAR(50))" + '"' 
                print("sssssssssssssssssssssssssssssss")
                print(add_columns)
                print("sssssssssssssssssssssssssssssss")
                continue
            if row[0] == "Player Name":
                continue

            result = db.session.execute("SELECT COUNT(*) FROM players WHERE name=:name AND team=:team", {"name":row[0], "team":row[1]}) #This is for updating data. If playerdata exists it is only being updated not inserted
            
            if result.fetchone()[0] > 0:
                sql = "UPDATE players SET games=:games, goals=:goals, assists=:assists, points=:points, plusminus=:plusminus, penalty=:penalty, shots=:shots, gwg=:gwg, ppg=:ppg, ppa=:ppa, shg=:shg, sha=:sha, hits=:hits, blocked=:blocked WHERE name=:name AND team=:team"           
                to_insert = {"name":row[0], "team":row[1], "games":row[3], "goals":row[4], "assists":row[5], "points":row[6], "plusminus":row[7],  #
                "penalty": row[8], "shots":row[9], "gwg":row[10], "ppg":row[11], "ppa":row[12], "shg":row[13], "sha":row[14], "hits":row[15], "blocked":row[16]}            
                db.session.execute(sql, to_insert)
                db.session.commit()
                continue



            to_insert = {"name":row[0], "team":row[1], "pos":row[2], "games":row[3], "goals":row[4], "assists":row[5], "points":row[6], "plusminus":row[7],  #
            "penalty": row[8], "shots":row[9], "gwg":row[10], "ppg":row[11], "ppa":row[12], "shg":row[13], "sha":row[14], "hits":row[15], "blocked":row[16]}
            db.session.execute(sql, to_insert)
            db.session.commit()