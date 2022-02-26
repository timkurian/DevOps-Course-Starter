class ViewModel:
    
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def doing_items(self):
        
        return [ item for item in self.items if item.status == 'Doing' ]