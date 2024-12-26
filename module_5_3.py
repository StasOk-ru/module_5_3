


class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует",'\n')
        else:
            for i in range(1, new_floor + 1):
                print(i)
            print("Приехали",'\n')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __len__(self):
        return self.floors

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors == other.floors
        return False

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other) #такое решение, а если много параметров?
        return False

    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        return False

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        return False

    def __gt__(self, other):#(>)
        if isinstance(other, int):
            return self.floors > other.floors
        return False

    def __ge__(self, other):#(>=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors >= other.floors
        return False

    def __lt__(self, other):#(<)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors < other.floors
        return False

    def __le__(self, other): #(<=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors <= other.floors
        return False

    def __ne__(self, other): #(!=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors != other.floors
        return False


h1 = House('ЖК Горский', 10)
h2 = House('ЖК Эльбрус', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__