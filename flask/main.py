from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
import json
import  datetime


with open('config.json' , 'r') as f:
    params = json.load(f)["params"]

local_server = True

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(20), unique=False)
    phoneno = db.Column(db.String(12), unique=False)
    msg = db.Column(db.String(120), unique=False)
    date = db.Column(db.String(12), unique=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(21), unique=False)
    content = db.Column(db.String(120), unique=False)
    tagline = db.Column(db.String(120), unique=False)
    date = db.Column(db.String(12), unique=False)
    img_file = db.Column(db.String(120), unique=False)
    post_by = db.Column(db.String(80), unique=False)


@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    return render_template("index.html" , params=params,posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",params=params)

@app.route("/edit",methods = ['GET','POST'])
def edit():
    if request.method == 'POST':
        box_title = request.form.get('title')
        tagline = request.form.get('tagline')
        slug = request.form.get('slug')
        content = request.form.get('content')
        img_file = request.form.get('img_file')
        post_by = request.form.get('post_by')

        post = Posts(title=box_title, tagline=tagline, slug=slug, content=content, img_file=img_file ,post_by=post_by,date=datetime.datetime.now())
        db.session.add(post)
        db.session.commit()



    return render_template("edit.html",params=params)


@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html" , params=params , post=post)

@app.route("/contact", methods =['GET','POST'] )
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')


        entry = Contacts(name=name,email=email,phoneno=phone,msg=message,date=datetime.datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html",params=params)


app.run(debug=True)