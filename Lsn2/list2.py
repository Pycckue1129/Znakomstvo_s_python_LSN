list_1 = []
for i in range(10):
    list_1.append(i)
print(list_1)
print(list_1.pop())  # Удаление последнего элемента в списке
print(list_1)
print(list_1.pop(0))  # Удаление элемента под индексом 0
print(list_1)
print(list_1.insert(2, 11))  # Вставка элемента под индекс, сначала указывается индекс
print(list_1)
print(list_1[1:9:2])  # Вывод от 1 до 9 с шагом 2

