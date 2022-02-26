
import pytest
from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

@pytest.fixture
def viewmodel() -> ViewModel:
    items=[]
    todo = Item( '1', 'Pick Up Laundry', 'Remember to pay a good tip aswell, they do a great job!', '24/04/2022', 'To Do')
    items.append(todo)
    view = ViewModel(items)
    
    return view



@staticmethod
def test_doing_items(viewmodel: ViewModel):

    # Arrange
    todo = Item( '1513', 'Check air pressure', 'Low air pressure causes inefficient energy use in vehicles', '24/04/2022', 'To Do')
    viewmodel.items.append(todo)

    # Act
    todos = viewmodel.doing_items
    # Assert
    assert len(todos) == 2
    assert todo in todos