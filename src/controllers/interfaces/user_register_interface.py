from abc import abstractmethod, ABC

class UserRegisterInterface(ABC):
    
    @abstractmethod
    def registry(self, username:str, password:str) ->dict:
        pass

