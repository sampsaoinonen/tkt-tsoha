import csv
from db import db

def get_data(filename):
    print("okei")

    with open("uploads/" + filename) as stats:                #here data from already downloaded csv-file 
        for row in csv.reader(stats, delimiter=","):    #is being parsed into sql-table        
            if row[0] == "\ufeff" :
                continue
            if any("name" and "team" in r.lower() for r in row):#lets collect names for columns of table                                            
                try:
                    add_columns = "CREATE TABLE players ( id SERIAL PRIMARY KEY, " + " TEXT, ".join(row) + " TEXT)"                 
                    db.session.execute(add_columns)
                    db.session.commit()
                    columns = row
                    db.session.execute("CREATE TABLE comments (id SERIAL PRIMARY KEY, content TEXT, players_id INTEGER REFERENCES players)")
                    db.session.commit()
                except:
                    continue
                continue
            
            rows = []   #because sql doesn't allow apostrophe mark(') in the middle of value let's replace ' with '' and it will be ok.
            for r in row:
                a = r.replace("'", "''")
                rows.append(a)
            try:
                sql = "INSERT INTO players (" + ", ".join(columns) + ")" + " VALUES ('" +  "', '".join(rows) + "')"
            except: 
                print("didnt happen")
                continue
            print(sql)
            
            db.session.execute(sql)
            db.session.commit()
            