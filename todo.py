from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Hasan/Desktop/TODOAPP/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean())
@app.route("/")
def index():
    todos=Todo.query.all()
    if len(todos)>0:

        return render_template("index.html",todos=todos)
    else:
        return render_template("index.html")
@app.route("/add", methods=["POST"])
def addTodo():
    title=request.form.get("newTodo")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/update/<string:id>")
def update(id):
    todo=Todo.query.filter_by(id=id).first()
    todo.complete=True
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def delete(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)