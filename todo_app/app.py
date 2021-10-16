from flask import Flask
from flask.templating import render_template
from todo_app.flask_config import Config
from todo_app.data import session_items
from flask import request

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todos = session_items.get_items()

    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    session_items.add_item(request.form['title'])
    return index()