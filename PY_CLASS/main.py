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

# nazwa klasy
class Coordinates5:
    # deklaracja z jednoczesna definicja atrybutow
    def __init__(yoyo, x, y, z):
        yoyo.x = x
        yoyo.y = y
        yoyo.z = z

# tworzenie obiektu klasy
o5 = Coordinates4(-5, 14, 77)

# usuniecie atrybutu (tylko po __init__())
del o5.x

# usuniecie obiektu
del o5

# G #

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("Jan", "Kowalski")
x.printname()

class Student(Person):
    pass

x = Student("Piotr", "Nowak")
x.printname()

class Teacher(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age
        print("Hello!")

y = Teacher("Elizeusz", "Kapustka", 30)
y.printname()
print(y.age)

class Teacher1(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        print("Hello!")

y1 = Teacher1("Elizeusz", "Kapustka")
y1.printname()

# H #

class Teacher2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        print("Hello!")
    
    def printname(self):
        return super().printname()

y2 = Teacher2("Elizeusz", "Kapustka")
y2.printname()

class Teacher3(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

    def printname(self):
        print(f"Witajcie! Nazywam się {self.fname} {self.lname}, mam {self.age} i jestem nauczycielem.")

y3 = Teacher3("Elizeusz", "Kapustka", 30)
y3.printname()

