import pytest
from mds_data_structures.mds_array import MDSArray

@pytest.fixture
def array():
    return MDSArray(1, 2, 3, 4)

def test_append(array):
    array.append(5)
    assert array[4] == 5

def test_getitem(array):
    assert array[0] == 1

def test_setitem(array):
    array[0] = 5
    assert array[0] == 5

def test_delitem(array):
    del array[0]
    assert len(array) == 3

def test_insert(array):
    array.insert(2, 6)
    assert array[2] == 6
    assert len(array) == 5
