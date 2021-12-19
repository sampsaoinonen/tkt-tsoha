from app import app
from flask import render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import players, downloader, comments, downloader, users
import os

players_columns = players.get_column_names() # easier way to get column names than typing them all
app.config['MAX_CONTENT_LENGTH'] = 10000 * 10000 # this will set up max size for uploaded file
uploads_dir = os.path.join('uploads')

@app.route("/")     
def index():        
    user_id = users.user_id()    
    return render_template("index.html", user_id=user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            flash("Wrong password or user doesn't exists!")
            return redirect("/login")            

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"]) ### tänne liian lyhyt salasana ja tunnus
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            flash("Passwords don't mach!")
            return redirect("/register")
        if len(password1) < 5 or len(password1) > 20:
            flash("Password has to be between 5 an 20 characters!")
            return redirect("/register")
        if len(username) < 3 or len(password1) > 20:
            flash("Username has to be between 3 an 20 characters!")
            return redirect("/register")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", error="Registration was aborted!")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    players_id = request.form["id"]
    fileid = request.form["fileid"]
    if users.user_id() == 0:
        flash("You you need to be logged in to leave a comment!")
        return redirect("/files/" + fileid + "/"+ players_id)        
    if len(content) == 0:
        flash("You are trying to send an empty comment!!")
        return redirect("/files/" + fileid + "/"+ players_id)
    if len(content) > 500:
        flash("Your comment is too long(over 500 characters)!")
        return redirect("/files/" + fileid + "/"+ players_id)
    comments.add_comment(content, players_id, users.user_id())    
    return redirect("/files/" + fileid + "/"+ players_id)
    
@app.route("/upload")     
def upload():           
    return render_template("upload.html")

@app.route("/uploader", methods = ["POST"])
def upload_file():
    f = request.files["file"]    
    if not f.filename.rsplit(".", 1)[1].lower() ==  "csv":    # here we check out that the uploaded file is csv-type        
        return render_template("error.html", error="You can only upload a csv-file!")        
    f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
    hidden = request.form.get("mycheckbox", default=False, type=bool)    
    if downloader.user_id_and_filename_used(f.filename, users.user_id()): # same filename from same user not allowed
        os.remove("uploads/" + f.filename)
        return render_template("error.html", error="You have already uploaded a csv-file named '" + f.filename 
        + "'!. If you are trying to upload a file with different content rename it.")    
    downloaded = downloader.get_data(f.filename, hidden, users.user_id())    
    if not downloaded:
        os.remove("uploads/" + f.filename)        
        return render_template("error.html", error="CSV-file have to be in the Rotowire form!")
    os.remove("uploads/" + f.filename)
    fileid = downloader.get_fileid(f.filename)
    return render_template("uploaded.html", filename=f.filename, fileid=fileid)

@app.route("/files")
def files():
    filenames_and_ids = downloader.get_filenames_and_ids(users.user_id())
    return render_template("files.html", filenames=filenames_and_ids)

@app.route("/files/<fileid>")
def stats(fileid):    
    filenames_and_ids = downloader.get_filenames_and_ids(users.user_id())    
    for f in filenames_and_ids:                
        if int(fileid) == f[0]: #lets check if user has rights to see the file
            result = players.get_players(fileid)
            return render_template("stats.html", players=result, players_columns=players_columns, fileid=fileid)    
    return render_template("error.html", error="This file doesn't exists or you have no rights to view this!")

@app.route("/files/<fileid>/organize/<organize>")
def organize(fileid, organize):             
    filenames_and_ids = downloader.get_filenames_and_ids(users.user_id())    
    for f in filenames_and_ids:        
        if int(fileid) == f[0]:
            result_organized = players.organize_players(organize, fileid)
            return render_template("stats.html", players=result_organized, players_columns=players_columns,fileid=fileid)    
    return render_template("error.html", error="This file doesn't exists or you have no rights to view this!")

@app.route("/files/<fileid>/organize/reverse/<organize>")
def organize_reverse(fileid, organize):    
    filenames_and_ids = downloader.get_filenames_and_ids(users.user_id())    
    for f in filenames_and_ids:        
        if int(fileid) == f[0]:
            result_organized = players.organize_players_reverse(organize, fileid)
            return render_template("stats.html", players=result_organized, players_columns=players_columns, fileid=fileid)    
    return render_template("error.html", error="This file doesn't exists or you have no rights to view this!")

@app.route("/files/<fileid>/<id>")
def player(fileid=None, id=None):
    
    filenames_and_ids = downloader.get_filenames_and_ids(users.user_id())
    for f in filenames_and_ids:
        if int(fileid) == f[0]:
            user_liked = users.get_liked(id, users.user_id())            
            result_player = players.get_player(id)
            result_comments = comments.get_comment(id)
            likes = players.get_likes(id)            
            return render_template("player.html", player=result_player, comments=result_comments, players_columns=players_columns, 
            fileid=fileid, likes=likes, user_liked=user_liked)
    return render_template("error.html", error="This file doesn't exists or you have no rights to view it!")

@app.route("/liked", methods=["POST"])
def liked():
    players_id = request.form["liked"]    
    fileid = request.form["fileid"]
    if users.user_id() == 0:
        flash("You you need to be logged in to leave a like!")
        return redirect("/files/" + fileid + "/"+ players_id)
    users.set_liked(players_id, users.user_id())            
    return redirect("/files/" + fileid + "/"+ players_id)
    