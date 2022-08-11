
from dbm import *
from flask import *

from dbm import inscom

from dbm import insert_grey
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/reg")
def register():
    return render_template("reg.html")

@app.route("/log")
def log():
    return render_template("login.html")
@app.route("/det")
def showdet():
    x=userdata()
    return render_template("display.html",elist=x)

@app.route("/details")
def details():
    data=userdata()
    return render_template("display.html", elist=data)
@app.route("/doc")
def doc():
    return render_template("doctorstrange.html")
@app.route("/docv")
def docv():
    return render_template("docv.html")
@app.route("/grey")
def gre():
    return render_template("thegray.html")
@app.route("/greyv")
def grev():
    return render_template("grayv.html")

@app.route("/justice")
def just():
    return render_template("justice.html")
@app.route("/justv")
def justv():
    return render_template("justv.html")

@app.route("/liger")
def lig():
    return render_template("liger.html")
@app.route("/ligv")
def ligv():
    return render_template("ligerv.html")

@app.route("/vikram")
def vik():
    return render_template("vikram.html")
@app.route("/vikramv")
def vikv():
    return render_template("vikramv.html")

@app.route("/john")
def john():
    return render_template("john.html")
@app.route("/johnv")
def johnv():
    return render_template("johnv.html")

@app.route("/about")
def abt():
    return render_template("aboutus.html")

@app.route("/insert_data",methods=["post"])
def ins():
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    age=request.form["age"]
    password=request.form["password"]
    t=(name,phone,email,age,password)
    insert(t)
    return redirect("/")

@app.route("/show_data", methods=["post"])
def shw():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=check(email)
    if t in t1:
         return redirect("/det")
    else:
         return redirect("/log")

@app.route("/edit")
def edit():
    email=request.args.get("email")
    info= single_user(email)
    return render_template("edit.html",i=info)

@app.route("/insagain",methods=["post"])
def insagain():
    email=request.form["email"]
    password=request.form["password"]
    t=(password,email)
    updateuser(t)
    return redirect("/details")

@app.route("/delete")
def delete():
    email=request.args.get("email")
    deleteuser(email)
    return redirect("/det")

@app.route("/add_review", methods=["post"])
def showr():
    uname=request.form["uname"]
    comment=request.form["comment"]
    t=(uname,comment)
    inscom(t)
    return redirect("/doc")
@app.route("/show_review") 
def show1():
    data=show()
    return render_template ("docv.html", val=data ) 

@app.route("/grey_review", methods=["post"])
def shower():
    uname1=request.form["uname1"]
    comment1=request.form["comment1"]
    t=(uname1,comment1)
    insert_grey(t)
    return redirect("/grey")

@app.route("/show_grey") 
def show2():
    data=show_grey()
    return render_template ("greyv.html", grey=data ) 

@app.route("/just_review", methods=["post"])
def shower1():
    uname2=request.form["uname2"]
    comment2=request.form["comment2"]
    t=(uname2,comment2)
    insert_just(t)
    return redirect("/justice")

@app.route("/show_just") 
def show3():
    data=show_just()
    return render_template ("justv.html", just=data ) 

@app.route("/lig_review", methods=["post"])
def shower2():
    uname3=request.form["uname3"]
    comment3=request.form["comment3"]
    t=(uname3,comment3)
    insert_lig(t)
    return redirect("/liger")

@app.route("/show_liger") 
def show4():
    data=show_lig()
    return render_template ("ligerv.html", lig=data ) 

@app.route("/vik_review", methods=["post"])
def shower3():
    uname4=request.form["uname4"]
    comment4=request.form["comment4"]
    t=(uname4,comment4)
    insert_vik(t)
    return redirect("/vikram")

@app.route("/show_vik") 
def show5():
    data=show_vik()
    return render_template ("vikramv.html", vik=data ) 

@app.route("/john_review", methods=["post"])
def shower4():
    uname5=request.form["uname5"]
    comment5=request.form["comment5"]
    t=(uname5,comment5)
    insert_john(t)
    return redirect("/john")

@app.route("/show_john") 
def show6():
    data=show_john()
    return render_template ("johnv.html", john=data ) 

if __name__ == "__main__":
    app.run(debug=True)