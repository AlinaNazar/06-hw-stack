import pytest
from stack import MyStackInt

@pytest.fixture
def stack():
    stack = MyStackInt()
    return stack

def test_max_single_item(stack):
    stack.push(12)
    assert stack.max() == 12

def test_max_stack_and_pop(stack):
    stack.push(12)
    stack.push(4)
    stack.push(5)
    stack.push(13)
    stack.push(12)
    assert stack.max() == 13
    assert stack.pop() == 12
    assert stack.pop() == 13
    assert stack.max() == 12

def test_two_equals_max_elements(stack):
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(6)
    assert stack.max() == 6
    assert stack.pop() == 6
    assert stack.max() == 6
    assert stack.pop() == 6
    assert stack.max() == 5

def test_pop_empty():
    stack = MyStackInt()
    with pytest.raises(IndexError):
        stack.pop()

def test_max_empty():
    stack = MyStackInt()
    with pytest.raises(IndexError):
        stack.max()

def test_pop_lifo(stack):
    stack.push(5)
    stack.push(10)

    assert stack.pop() == 10
    assert stack.pop() == 5
    assert stack.is_empty()

@pytest.mark.parametrize(
    "items, expected",
    [
        ([-5, -10, -3], -3),
        ([-500, -1000, -600], -500),
        ([-5, -1, 0], 0),
    ]
)

def test_negative_max(stack, items, expected):
    for item in items:
        stack.push(item)

    assert stack.max() == expected

def test_reuse_after_empty():
    stack = MyStackInt()
    stack.push(5)
    stack.push(10)
    stack.push(17)
    while not stack.is_empty():
        stack.pop()
    assert stack.is_empty()
    stack.push(11)
    assert stack.max() == 11