class Accout:
    def __init__(self,id=0,balance=1000000,annualInterestRate=0):
        self.__id = id
        self.__bal = balance
        self.__annual  = annualInterestRate / 100

    def getInfo(self):
        return self.__id , self.__bal , self.getMonthlyInterestRate() , self.getMonthlyInterest()

    def setChange(self,id,bal,annual):
        self.__id = id
        self.__bal = bal
        self.__annual = annual

    def getMonthlyInterestRate(self):
        return self.__annual / 12

    def getMonthlyInterest(self):
        return self.__bal * self.getMonthlyInterestRate()

    def withdraw(self,draw):
        self.__bal = self.__bal - draw

    def deposit(self,posit):
        self.__bal = self.__bal + posit


