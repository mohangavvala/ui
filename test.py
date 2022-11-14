from abc import abstractmethod,ABC

class Test(ABC):
    @abstractmethod
    def m1(self):
        print("m1")
    @abstractmethod
    def m2(self):
        print("m2")
