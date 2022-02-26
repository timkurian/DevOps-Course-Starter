
import pytest
from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

@pytest.fixture
def viewmodel() -> ViewModel:
    items=[]
    doing = Item( '1', 'Pick Up Laundry', 'Remember to pay a good tip aswell, they do a great job!', '24/04/2022', 'Doing')
    items.append(doing)
    view = ViewModel(items)
    
    return view



@staticmethod
def test_doing_items(viewmodel: ViewModel):

    # Arrange
    doing = Item( '1513', 'Check air pressure', 'Low air pressure causes inefficient energy use in vehicles', '24/04/2022', 'Doing')
    viewmodel.items.append(doing)

    # Act
    doings = viewmodel.doing_items
    # Assert
    assert len(doings) == 2
    assert doing in doings

