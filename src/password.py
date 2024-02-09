
class Password:
    
    @classmethod
    def is_valid(cls, password: str) -> bool:
        return len(password) >= 8
