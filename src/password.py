
class Password:
    
    @classmethod
    def is_valid(cls, password: str) -> bool:
        # return False
        return len(password) >= 8 and \
               any(c.isupper() for c in password) and \
               any(c.islower() for c in password) and \
               any(c.isdigit() for c in password) and \
               any(c == "_" for c in password)
