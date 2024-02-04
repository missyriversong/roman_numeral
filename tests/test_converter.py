import pytest

# run python -m pytest
from katas.numeral.dict import dict


@pytest.fixture   #pass params? 
def n_dict():
    return dict()

def test_create_dict(n_dict):
    assert isinstance(n_dict, dict)

def add_pair(n_dict, key, value):
    assert n_dict.add(key, value) 
  
def get_value(self, key):
    assert n_dict.get_value(key) == "value"
    

