from flask import Flask
from flask.templating import render_template
from todo_app.flask_config import Config
from todo_app.data import session_items
from flask import request


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todos = session_items.get_items()
    
    return render_template('index.html', todos=todos)

@app.route('/modify/<id>')
def modify_todo(id):
    todo = session_items.get_item(id)
    return render_template('modify.html', todo=todo)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    session_items.add_item(request.form['title'])
    return index()

@app.route('/update_todo', methods=['POST'])
def update_todo(): 
    item = session_items.get_item(request.form['id'])
    item['status'] = request.form['status']
    session_items.save_item(item)    
    return index()

@app.route('/remove_todo', methods=['POST'])
def remove_todo():   
    session_items.remove_item(request.form['id'])
    return index()

