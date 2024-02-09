
class Password:
    
    MINIMUM_LENGTH = 8
    
    @classmethod
    def is_valid(cls, password: str) -> bool:
        return len(password) >= cls.MINIMUM_LENGTH and \
               any(c.isupper() for c in password) and \
               any(c.islower() for c in password) and \
               any(c.isdigit() for c in password) and \
               any(c == "_" for c in password)
