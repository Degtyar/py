#!/usr/bin/python3

import buildroom as a

oboi =      a.wallPapers(1000, 1.05, 10)
paint =     a.paint(5000, 2, 0.3)
laminat =   a.laminate(1850, 1.2, 0.2, 16)

komnata1 = a.room('Кухня', 3, 2.75, 4, 1.5, 1.3)
komnata2 = a.room('Зал', 5, 2.75, 4, 1.5, 1.3)
komnata3 = a.room('Спальня', 4, 2.75, 3, 1.5, 1.3)
kvartira = a.apartment(komnata1, komnata2, komnata3)

kvartira.smeta(oboi, paint, laminat)

print('________________________________________')
print('- Дорого, кухню сделаю позже, давайте пока коридор сделаем')
print('________________________________________')

komnata4 = a.room('Коридор', 2, 2.75, 6, 0, 3)
kvartira.addRoom(komnata4)
kvartira.delRoom(komnata1)
kvartira.smeta(oboi, paint, laminat)

print('________________________________________')
print('- Отлично, еще дороже, обои потом поклею')
print('_______________________________________')
kvartira.smeta(paint, laminat)
