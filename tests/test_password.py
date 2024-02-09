
from src.password import Password

def test_minimun_eight_length():
    
    invalid_password = "3"*3
    
    assert not Password.is_valid(invalid_password)


def test_at_least_one_uppercase():
    
    invalid_password = "abcdefgh"
    
    assert not Password.is_valid(invalid_password)
    
def test_at_least_one_lowercase():
    
    invalid_password = "ABCDEFGH"
    
    assert not Password.is_valid(invalid_password)


def test_at_least_one_number():
    
    invalid_password = "AbCDEFGH"
    
    assert not Password.is_valid(invalid_password)
