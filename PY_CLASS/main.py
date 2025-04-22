# A #

# nazwa klasy
class MyClass:
    # zaznaczenie, ze klasa ma byc pusta
    pass

# tworzenie obiektu klasy
o = MyClass()

# B #

# nazwa klasy
class Coordinates:
    # atrybuty klasy
    x = 10
    y = 15
    z = -30

# tworzenie obiektu klasy
o1 = Coordinates()

# odniesienie się do atrybutow
print(f"x: {o1.x} / y: {o1.y} / z: {o1.z}")

# C #

# nazwa klasy
class Coordinates2:
    # atrybuty klasy
    x = 10
    y = 15
    z = -30

    # metody klasy - self oznacza, ze odnosimy sie do elementow klasy
    def printCoordinates(self):
        print(f"x: {self.x} / y: {self.y} / z: {self.z}")

# tworzenie obiektu klasy
o2 = Coordinates2()

# zastosowanie metody na obiekcie klasy
o2.printCoordinates()

# D #

# nazwa klasy
class Coordinates3:
    # atrybuty klasy
    x = 10
    y = 15
    z = -30

    # metody klasy - self oznacza, ze odnosimy sie do elementow klasy
    def __str__(self):
        return f"x: {self.x} / y: {self.y} / z: {self.z}"

# tworzenie obiektu klasy
o3 = Coordinates3()

# zastosowanie funckji tekstowej na obiekcie
print(o3)

# E #

# nazwa klasy
class Coordinates4:
    # deklaracja z jednoczesna definicja atrybutow
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # metody klasy - self oznacza, ze odnosimy sie do elementow klasy
    def __str__(self):
        return f"x: {self.x} / y: {self.y} / z: {self.z}"

# tworzenie obiektu klasy
o4 = Coordinates4(-5, 14, 77)

# zastosowanie funckji tekstowej na obiekcie
print(o4)

# F #

