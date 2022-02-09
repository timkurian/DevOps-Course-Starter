import os
import requests
from todo_app.data.Item import Item


TRELLO_API_URL = "https://api.trello.com"
TRELLO_APP_KEY=os.getenv('TRELLO_APP_KEY')
TRELLO_TOKEN=os.getenv('TRELLO_TOKEN')
BOARD_ID = os.getenv('BOARD_ID')

"""
    Gets the lists from the board, then based on the field name , returns the matching value
    Useful for getting a list object either based on idList key, or name
"""
def __get_list_from_list_name(field_name, list_name):
    response_list = requests.get(f"{TRELLO_API_URL}/1/boards/{BOARD_ID}/lists?key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}")
    return [ x for x in response_list.json() if x[field_name] == list_name ][0]

def get_items():
    response_items = requests.get(f"{TRELLO_API_URL}/1/boards/{BOARD_ID}/cards?key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}")
    
    items = []
    for card in response_items.json():
        list_name = __get_list_from_list_name('id',card['idList']) 
        item = Item.from_trello_card(card, list_name )
        items.append(item)
    items.sort(key=lambda x: x.status)
    return items

def get_item(id):
    response_item = requests.get(f"{TRELLO_API_URL}/1/cards/{id}?key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}")
    card = response_item.json()
    list_name = __get_list_from_list_name('id', card['idList']) 

    return Item.from_trello_card(response_item.json(), list_name)


def add_item(title,description,duedate):
    list_name = __get_list_from_list_name('name', "To Do") 
    requests.post(f"{TRELLO_API_URL}/1/cards?idList={list_name['id']}&key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}",  data={'name': f"{title}",'desc': f"{description}", 'due': f"{duedate}" })

def save_item(item):
    list_name = __get_list_from_list_name('name', item.status)
    r = requests.put(f"{TRELLO_API_URL}/1/cards/{item.id}?key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}", data={'name': f"{item.name}",'idList':list_name['id'] ,'desc': f"{item.description}", 'due': f"{item.duedate}" }  )
    

def remove_item(id):
    requests.delete(f"{TRELLO_API_URL}/1/cards/{id}?key={TRELLO_APP_KEY}&token={TRELLO_TOKEN}")

