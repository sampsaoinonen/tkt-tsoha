import csv
from db import db

def get_data():

    with open("nhl-stats.csv") as stats:                #here data from already downloaded csv-file 
        for row in csv.reader(stats, delimiter=","):    #is being parsed into sql-table        
            if row[0] == "\ufeff" :
                continue
            if any("name" and "team" in r.lower() for r in row):#lets collect names for columns of table                            
                
                #columns = '"' + "INSERT INTO players (" + ", ".join(row) + ") VALUES (:" + ", :".join(row)  +')"'
                #add_columns = '"' + "ALTER TABLE players ADD(" + " CHAR(50), ".join(row) + "CHAR(50))" + '"' 
                columns = row
                continue
                add_columns = "CREATE TABLE players ( " + " char(50), ".join(row) + " char(50))" 
                print("ssssssssssssssssssssssssssssss")
                print(add_columns)
                print("sssssssssssssssssssssssssssssss")
                db.session.execute(add_columns)
                db.session.commit()
                continue
            
            sql = "INSERT INTO players (" + ", ".join(columns) + ")" + " VALUES (:" +  ", :".join(columns) + ")"
            
            
            #sql = '"' + "INSERT INTO players (" + ", ".join(row) + ") VALUES (:" + ", :".join(row)  +')"'
            

            to_insert = "{"
            i = 0
            for column in columns:
                to_insert += '"' + column + '"' + ":" + '"' + row[i] + '"' + ","
                i += 1
            to_insert = to_insert[:-1] + "}"
            print(sql)
            print(to_insert)
            
            db.session.execute(sql, to_insert)
            db.session.commit()
            
            continue    
           
            sql =  "INSERT INTO players (Player_name, Team) VALUES (:Player_name, :Team)" 
            to_insert = {"Player_name":row[0], "Team":row[1]}
            db.session.execute(sql, to_insert)
            db.session.commit()

            sql =  "INSERT INTO players (Player_name, Team) VALUES (:Player_name, :Team)" 
            to_insert = {"Player_name":"jesss", "Team":"okei"}
            db.session.execute(sql, to_insert)
            db.session.commit()
            continue