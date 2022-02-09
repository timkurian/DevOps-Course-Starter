from datetime import datetime

class Item:
    def __init__(self, id, name, description, duedate, status = 'To Do'):
        self.id = id
        self.name = name
        self.description = description
        self.duedate = duedate
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        date = ""
        if card['due'] != None:
            date = datetime.fromisoformat(card['due'][:-1]).date()
        
        return cls(card['id'], card['name'], card['desc'], date, list['name']) 


    '''
        Helpful to string representation of the object
        useful when debugging.
    '''
    def __str__(self):
     return f"Item: [ id = {self.id} , name = {self.name}, description = {self.description}, duedate = {self.duedate}, status = {self.status} ]"