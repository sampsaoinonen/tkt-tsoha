from app import app
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
import players, downloader, comments, downloader, users
import os

if players.checkTableExists() == False:
    downloader.get_data()
players_columns = players.get_column_names()
app.config['MAX_CONTENT_LENGTH'] = 5000 * 5000 # this will set up max size for uploaded file
uploads_dir = os.path.join('uploads')


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
            return render_template("error.html", error="Wrong password or username!")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", error="Passwords don't mach!")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", error="Registration was aborted!")
   

@app.route("/")     
def index():    
    upload_link = ""
    if users.user_id() != 0:
        upload_link = "upload"
    result = players.get_all()
    return render_template("stats.html", players=result, players_columns=players_columns, log_link=users.log_link(), upload_link=upload_link)

@app.route("/<int:id>")
def page(id):
    result_player = players.get_player(id)    
    result_comments = comments.get_comment(id)
    logged_comment = "(you need to be logged in)"
    if users.user_id() != 0:
        logged_comment = ""
    return render_template("player.html", player=result_player, comments=result_comments, players_columns=players_columns, log_link=users.log_link(), logged_comment=logged_comment)

@app.route("/organize/<organize>")
def org(organize):          
    upload_link = ""
    if users.user_id() != 0:
        upload_link = "upload"
    result_organized = players.organize_players(organize)
    return render_template("stats.html", players=result_organized, players_columns=players_columns, log_link=users.log_link(), upload_link=upload_link)

@app.route("/organize/reverse/<organize_reverse>")
def org_reverse(organize_reverse):          
    upload_link = ""
    if users.user_id() != 0:
        upload_link = "upload"
    result_organized = players.organize_players_reverse(organize_reverse)
    return render_template("stats.html", players=result_organized, players_columns=players_columns, log_link=users.log_link(), upload_link=upload_link)

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    players_id = request.form["id"]
    if users.user_id() == 0:
        return render_template("error.html", error="You you need to be logged in to leave a comment!")
    if len(content) == 0:
        return render_template("error.html", error="You are trying to send an empty comment!")
    if len(content) > 500:
        return render_template("error.html", error="Your comment is too long(over 500 characters)!")
    comments.add_comment(content, players_id, users.user_id())    
    return redirect("/" + players_id)

@app.route("/upload")     
def upload():           
    return render_template("upload.html")

@app.route('/uploader', methods = ["POST"])
def upload_file():
    f = request.files['file']    
    if not f.filename.rsplit('.', 1)[1].lower() ==  "csv":    # here we check out that the uploaded file is csv-type
        return render_template("error.html", error="You can only upload a csv-file!")    
    
    f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
    print("*****")
    downloader.get_data(f.filename)
    print("*****")
    return render_template("uploaded.html", filename=f.filename)

#return redirect("/<int:request.form.id>")