class Tesla:

    kolor = "biały"

    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def __biegWyzej(self):
        if self.__bieg <= 6:
            self.__bieg += 1
            print(self.__bieg)

    def biegNizej(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
            print(self.__bieg)

    def przyspiesz(self):
        if self.__silnik is True and self.__bieg > 0:
            self.__predkosc += 10
            print(self.__predkosc)

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
            print(self.__predkosc)
            # print(self.kolor)

car = Tesla()
car.uruchom()
car.__biegWyzej()
car.__silnik = False
car.przyspiesz()
car.przyspiesz()
car.przyspiesz()
car.__biegWyzej()




