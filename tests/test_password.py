
from src.password import Password

VALID_PASSWORD = "AABBaa1_"

def test_minimun_eight_length():
    
    invalid_password = VALID_PASSWORD[:3]
    
    assert not Password.is_valid(invalid_password)
    
def test_is_valid():
    
    assert Password.is_valid(VALID_PASSWORD)


def test_at_least_one_uppercase():
    
    invalid_password = VALID_PASSWORD.lower()
    
    assert not Password.is_valid(invalid_password)
    
def test_at_least_one_lowercase():
    
    invalid_password = VALID_PASSWORD.upper()
    
    assert not Password.is_valid(invalid_password)


def test_at_least_one_number():
    
    invalid_password = VALID_PASSWORD.replace("1", "A")
    
    assert not Password.is_valid(invalid_password)

def test_at_least_one_underscore():
    
    invalid_password = VALID_PASSWORD.replace("_", "A")
    
    assert not Password.is_valid(invalid_password)