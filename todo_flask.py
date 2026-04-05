from todo import TodoManager
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
td=TodoManager()
@app.route("/")
def index():
    data = td.view_data()
    return render_template("todo.html",data=data)
@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content")
    td.add_todo(content)
    return redirect("/")
@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    td.set_keyword(keyword)
    return redirect("/")
@app.route("/sort", methods=["POST"])
def sort():
    column = request.form.get("column")
    td.set_sort(column)
    return redirect("/")
@app.route("/filter", methods=["POST"])
def filter():
    category = request.form.get("category")
    if category == "all":
        td.reset_state()
        return redirect("/")
    td.set_filter_category(category)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
