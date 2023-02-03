from flask import Flask,render_template,request
import sqlite3 as sql

app=Flask("__name__")

@app.route("/")
def show():
    conn=sql.connect("crud.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from data")
    data=cur.fetchall()
    return render_template("table.html",data=data)

@app.route("/insert", methods=["post","get"])
def insert():
  if request.form.get("id")!=None:  
    id=request.form.get("id")
    username=request.form.get("username")
    rollnumber=request.form.get("rollnumber")
    language=request.form.get("language")
    conn=sql.connect("crud.db")
    cur=conn.cursor()
    cur.execute("insert into data (id,username,rollnumber,language) values (?,?,?,?)",(int(id),username,int(rollnumber),language))
    conn.commit()
  return render_template("index.html")   

@app.route("/update/<id>", methods=["post","get"])
def update(id):
    if request.form.get("id")!=None and request.method=="POST":
        username=request.form.get("username")
        rollnumber=request.form.get("rollnumber")
        language=request.form.get("language")
        conn=sql.connect("crud.db")
        cur=conn.cursor()
        cur.execute("UPDATE DATA SET USERNAME=? , ROLLNUMBER=?, LANGUAGE=? WHERE ID=?",(username,int(rollnumber),language,int(id)))
        conn.commit() 
        return render_template("index.html")
    conn=sql.connect("crud.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from data where ID=?",(int(id),))
    a=cur.fetchone()
    return render_template("create.html",data=a)
if __name__=="__main__":
    app.run(debug=True)

