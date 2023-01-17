from flask import *
import sqlite3
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():
    return render_template("add.html");
@app.route("/savedetails", methods=["POST","GET"])
def saveDetails():
    msg="msg"
    if request.method =="POST":
        try:
            name=request.form["name"]
            email=request.form["email"]
            address=request.form["address"]
            with sqlite3.connect("employeedetails.db") as c:
                cur=c.cursor()
                cur.execute("INSERT into Employees(name, email, address) values(?,?,?)",(name, email,address))
                c.commit()
                msg="Details successfully added"
        except:
            c.rollback()
            msg="cannot add data"
        finally:
            return render_template("success.html", msg=msg)
            c.close()

@app.route("/view")
def view():
    c= sqlite3.connect("employeedetails.db")
    c.row_factory=sqlite3.Row
    cur=c.cursor()
    cur.execute("select * from Employees")
    rows= cur.fetchall()
    return render_template("view.html",rows=rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleteRecord():
    id= request.form["id"]
    with sqlite3.connect("employeedetails.db") as c:
        try:
            cur = c.cursor()
            cur.execute("delete from Employees where id=?",id)
            msg="record deleted successfully"
        except:
            msg="cant delete data"
        finally:
            return render_template("delete_record.html",msg=msg)

if __name__=="__main__":
    app.run(host='localhost',port=888)


