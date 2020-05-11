import math
#클래스를 쓸때 self만 있는것은 호출할때 인자가 필요없다.
class Circle:
    def __init__(self,radius=1):
        self.__radius =radius  #__radius가 이 클래스내에서 사용되는 변수이름
        # __radius에 언더바 두개를 붙혀주므로써 클래스내 변수를 바로 못부름 getRadius등으로 불러야함.
    def getperameter(self):
        return 2* self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius*math.pi

    def getRadius(self):
        return self.__radius

    def setradius(self,radiuss):
        self.__radius = radiuss #새로준 인자의 값을 기존에있던 _radius에 새로 바꾸겠다.