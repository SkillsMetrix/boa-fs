from abc import ABC,abstractclassmethod

class RBI(ABC):
    @abstractclassmethod
    def deposit(self):
        pass
    def demoFun(self):
        print("demo method")


class SBI(RBI):
    def deposit(self):
        return "FD Opened"
    def openFD(self):
        return "FD Opened"
    def demoFun(self):
        print("SBI method")

bank= SBI()
print(bank.deposit())
print(bank.openFD())
print(bank.demoFun())