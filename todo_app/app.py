from flask import Flask, request, redirect, url_for
from flask.templating import render_template
from todo_app.data.ViewModel import ViewModel
from todo_app.flask_config import Config
from todo_app.data import trello_items

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todos = trello_items.get_items()
    item_view_model = ViewModel(todos)
    return render_template('index.html', view_model=item_view_model)

@app.route('/modify/<id>')
def modify_todo(id):
    todo = trello_items.get_item(id)
    return render_template('modify.html', todo=todo)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    trello_items.add_item(request.form['title'],request.form['description'],request.form['duedate'])
    return redirect(url_for('index'))

@app.route('/update_todo', methods=['POST'])
def update_todo(): 

    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    duedate = request.form['duedate']
    description = request.form['description']
    trello_items.save_item(id,name,status,duedate,description)    
    return redirect(url_for('index'))

@app.route('/remove_todo', methods=['POST'])
def remove_todo():   
    trello_items.remove_item(request.form['id'])
    return redirect(url_for('index'))

