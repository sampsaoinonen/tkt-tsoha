import csv
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import urllib.request

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL") ## this one works locally
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1) #this one works in Heroku   
db = SQLAlchemy(app)


with open("nhl-stats.csv") as stats:                #here data from already downloaded csv-file 
    for row in csv.reader(stats, delimiter=","):    #is being parsed into sql-table        
        if(row[0] == "\ufeff" or row[0] == "Player Name"):  #first lines with other than player data is not included
           continue

        result = db.session.execute("SELECT COUNT(*) FROM players WHERE name=:name AND team=:team", {"name":row[0], "team":row[1]}) #This is for updating data. If playerdata exists it is only being updated not inserted
        if(result.fetchone()[0] == 1):           
            continue    #Missing sql update here

        sql =  "INSERT INTO players (name, team, pos, games, goals, assists, points, plusminus, penalty, shots, gwg, ppg, ppa, shg, sha, hits, blocked) VALUES (:name, :team , :pos, :games, :goals, :assists, :points, :plusminus, :penalty, :shots, :gwg, :ppg, :ppa, :shg, :sha, :hits, :blocked)"
        to_insert = {"name":row[0], "team":row[1], "pos":row[2], "games":row[3], "goals":row[4], "assists":row[5], "points":row[6], "plusminus":row[7],  #
        "penalty": row[8], "shots":row[9], "gwg":row[10], "ppg":row[11], "ppa":row[12], "shg":row[13], "sha":row[14], "hits":row[15], "blocked":row[16]}
        db.session.execute(sql, to_insert)
db.session.commit()


@app.route("/")     
def index():
    result = db.session.execute("SELECT * FROM players")
    players = result.fetchall()
    return render_template("index.html", players=players)

@app.route("/<int:id>")
def page(id):
    result_player = db.session.execute("SELECT * FROM players WHERE id=:id", {"id":id})
    player = result_player.fetchone()
    result_comments = db.session.execute("SELECT * FROM comments WHERE players_id=:id", {"id":id})
    comments = result_comments.fetchall()

    return render_template("player.html", player=player, comments=comments)
    
@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    players_id = request.form["id"]
    if len(content) > 10:
        return render_template("error.html", error="Your comment is too long(over 5000 characters)!")
    sql = "INSERT INTO comments (content, players_id) VALUES (:content, :players_id)"
    db.session.execute(sql, {"content":content, "players_id":players_id})
    db.session.commit()        
    print(players_id)
    return redirect("/" + players_id)


#return redirect("/<int:request.form.id>")
