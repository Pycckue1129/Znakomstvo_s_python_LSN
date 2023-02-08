# Операции со множествами в Python

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # Копирует множество
u = a.union(b)  # Объеденяет и оставляет уникальные значения
i = a.intersection()  # Находит одинаковые элементы
dl = a.difference(b)  # Находит разность
dr = b.difference(a)  # Находит разность
q = a.union(b).difference(a.intersection(b))  # Все вместе  
print(u)
print(i)
print(dl)
print(dr)
print(q)