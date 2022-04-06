from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add')
def Add_Emp():
    return render_template("add.html")

@app.route('/search')
def Search_Emp():
    return render_template("search.html")

@app.route('/update')
def Update_Emp():
    return render_template("update.html")

@app.route('/delete')
def Delete_Emp():
    return render_template("delete.html")

if __name__ == "__main__":
    app.run()