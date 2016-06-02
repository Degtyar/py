#!/usr/bin/python3
import math


class buildMaterial():
    """ Базовый класс строительных материалов"""

    def __init__(self, cost):
        self.cost = cost

class wallPapers(buildMaterial):
    """Класс обои, стоимость / ширина / длинна"""

    n = 'Обои'
    def __init__(self, cost, width, long):
        super().__init__(cost)
        self.w = width
        self.l = long
        self.area = self.w * self.l


class paint(buildMaterial):
    """Класс краска, стоимость / вес / расход"""

    n = 'Краска'
    def __init__(self, cost, weight, decreases):
        super().__init__(cost)
        self.w = weight
        self.d = decreases
        self.area = self.w / self.d


class laminate(buildMaterial):
    """Класс ламинат, стоимость / длинна / ширина / количество"""

    n = 'Ламинат'
    def __init__(self, cost, long, width, count):
        super().__init__(cost)
        self.l = long
        self.w = width
        self.c = count
        self.area = self.w * self.c * self.l


class room():
    """Класс комната, наименование / ширина / высота / длинна / ширна окна / ширина двери"""

    def __init__(self, name, width, height, long, windowWidht, doorWidth):
        self.n = name
        self.w = width
        self.h = height
        self.l = long
        self.wW = windowWidht
        self.dW = doorWidth
        self.wallArea = (self.w * 2 + self.l * 2 - self.wW - self.dW) * self.h
        self.ceilingFloorArea = (self.w * self.l)

    def doIt(self, object):
        self.area = self.wallArea if object.n == 'Обои' else self.ceilingFloorArea
        if object.area != 0:
            count = math.ceil(self.area / object.area)
        else:
            count = 0
        cost = count * object.cost
        return (object.n, object.cost, count, cost)

    def smeta (self, *objects):
        summ = 0
        print(('[%s: ширина: %.2f м, длинна:%.2f м, высота: %.2f м]')%(self.n ,self.w, self.l, self.h))
        for object in objects:
            itogCost = self.doIt(object)
            print(('%s \t\t %.2fx%.2f=%.2f \t руб.')%(itogCost))
            summ += itogCost[3]
        return summ

class apartment():
    """Класс квартира, комнаты"""

    def __init__(self, *rooms):
        self.room = list(rooms)

    def smeta(self, *object):
        summ = 0
        for room in self.room:
            summ += room.smeta(*object)
        print('_________________________________')
        print('Итого: \t\t\t\t %.2f руб '%(summ))

    def addRoom(self,room):
       self.room.append(room)

    def delRoom(self,room):
        self.room.remove(room)


