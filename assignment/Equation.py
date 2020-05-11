
class QuadraticEquation:

    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getparamiter(self):
        return self.__a ,self.__b,self.__c

    def getDiscriminant(self):
        return (self.__b *self.__b)- 4 * self.__a * self.__c

    def getRoot1(self):
        if(self.getDiscriminant()> 0 or self.getDiscriminant() == 0):
            return (-self.__b + (self.getDiscriminant())**0.5) / 2*self.__a
        else :
            return 0

    def getRoot2(self):
        if (self.getDiscriminant() > 0 ):
             return (-self.__b - (self.getDiscriminant()**0.5)) / 2*self.__a
        else:
            return 0