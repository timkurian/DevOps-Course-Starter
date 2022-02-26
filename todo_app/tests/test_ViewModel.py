
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



@staticmethod
def test_todo_items(viewmodel: ViewModel):

    # Arrange
    todo = Item( '1413', 'Solve World Hunger', 'Food waste and world hunger co-exist. Formulate a plan to end this', '01/01/2023', 'To Do')
    viewmodel.items.append(todo)

    # Act
    todos = viewmodel.todo_items
    # Assert
    assert len(todos) == 1
    assert todo in todos
    assert todo.id == '1413'
    assert todo.name == 'Solve World Hunger'
    assert todo.description == 'Food waste and world hunger co-exist. Formulate a plan to end this'
    assert todo.duedate == '01/01/2023'
    assert todo.status == 'To Do'


@staticmethod
def test_done_items(viewmodel: ViewModel):

    # Arrange
    done = Item( '1613', 'Run for the office of US presedent', 'Ask not what your country can do for you', '01/01/2000', 'Done')
    viewmodel.items.append(done)

    # Act
    dones = viewmodel.done_items
    # Assert
    assert len(dones) == 1
    assert done in dones
    assert done.id == '1613'
    assert done.name == 'Run for the office of US presedent'
    assert done.description == 'Ask not what your country can do for you'
    assert done.duedate == '01/01/2000'
    assert done.status == 'Done'