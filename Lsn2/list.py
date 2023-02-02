list_1 = []  # первый способ создания листа
list_1 = list()  # второй
list_1 = [1, 2, 3, 8]

for i in list_1:
    print(i, end=', ')

print(*list_1)  # * - открыть список (убрать скобки знаки)

print(len(list_1))  # размер списка

list_1.append(8)  # добавление элемента в конец списка
print(list_1[4])
