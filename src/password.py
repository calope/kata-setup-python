
class Password:
    
    MINIMUM_LENGTH = 8
    AT_LEAST_ONE = (lambda c: c.isupper(),
                    lambda c: c.islower(),
                    lambda c: c.isdigit(),
                    lambda c: c == "_" )
    
    @classmethod
    def is_valid(cls, password: str) -> bool:
        
        return len(password) >= cls.MINIMUM_LENGTH and \
               all(any(rule(c) for c in password) 
                    for rule in cls.AT_LEAST_ONE)
