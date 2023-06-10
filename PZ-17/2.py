<<<<<<< HEAD
# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Geo:
    sh = 10
    vis = 14

    def perimetr(self):
        return print(self.sh+self.vis)
    def plsh(self):
        return print(self.sh*self.vis)

class Pr(Geo):
    p = 20

class Kv(Geo):
    def perimetr(self):
        return print(self.sh*2)
    def plsh(self):
=======
# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Geo:
    sh = 10
    vis = 14

    def perimetr(self):
        return print(self.sh+self.vis)
    def plsh(self):
        return print(self.sh*self.vis)

class Pr(Geo):
    p = 20

class Kv(Geo):
    def perimetr(self):
        return print(self.sh*2)
    def plsh(self):
>>>>>>> a10112b242c7042c5ee5180ea2ad57437da52535
        return  print(self.sh*2)