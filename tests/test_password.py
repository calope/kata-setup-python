
from src.password import Password

def test_minimun_eight_length():
    
    invalid_password = "3"*3
    
    assert not Password.is_valid(invalid_password)
