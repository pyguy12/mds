import pytest
from pytest_mock import mocker
from mds_animators.mds_array_animator import MDSArrayAnimator
from mds_data_structures.mds_array import MDSArray

@pytest.fixture
def array(mocker):
    animator_mock = mocker.MagicMock(spec=MDSArrayAnimator)
    return MDSArray(elementsList=[1, 2, 2, 3, 4], animator=animator_mock)

def test_append(array):
    array.append(5)
    assert array[5] == 5

def test_getitem(array):
    assert array[0] == 1

def test_setitem(array):
    array[0] = 5
    assert array[0] == 5

def test_delitem(array):
    del array[0]
    assert len(array) == 4

def test_insert(array):
    array.insert(2, 6)
    assert array[2] == 6
    assert len(array) == 6

def test_contains(array):
    assert (5 in array) is False
    assert (1 in array) is True

def test_index(array):
    assert array.index(1) == 0
    assert array.index(2) == 1
    with pytest.raises(ValueError):
        array.index(5) # Should raise ValueError as 5 is not in the list

def test_count(array):
    assert array.count(2) == 2
    assert array.count(5) == 0

def test_extend(array):
    array.extend([5, 6, 7])
    assert len(array) == 8
    assert array[5] == 5
    assert array[6] == 6
    assert array[7] == 7

def test_pop(array):
    assert array.pop() == 4
    assert len(array) == 4
    assert array.pop(1) == 2
    assert len(array) == 3

def test_reverse(array):
    array.reverse()
    assert array[0] == 4
    assert array[3] == 2
    assert array[4] == 1

def test_sort(array):
    array.sort()
    assert array[0] == 1
    assert array[1] == 2
    assert array[2] == 2
    assert array[3] == 3
    assert array[4] == 4

def test_insert_calls_animate_insertion(array):
    array.insert(0, 'value')
    array.animator.animate_insertion.assert_called_once_with('value', 0)

def test_animator_type_check(mocker):
    incorrect_animator = mocker.Mock()  # Create a Mock object which is not an MDSArrayAnimator
    with pytest.raises(TypeError):  # Expect a TypeError to be raised
        MDSArray([], incorrect_animator)

def test_animator_init_call(mocker):
    animator_mock = mocker.MagicMock(spec=MDSArrayAnimator)
    elements = [1, 2, 3]
    array = MDSArray(elements, animator_mock)
    animator_mock.animate_init.assert_called_once_with(elements)