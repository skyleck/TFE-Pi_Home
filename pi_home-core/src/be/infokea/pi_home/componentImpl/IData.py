import abc

class IData(abc.ABC):
    
    @abc.abstractmethod
    def constructValues(self,user):
        pass
