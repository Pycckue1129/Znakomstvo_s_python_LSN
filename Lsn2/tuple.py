# Кортежи

t = ()
print(type(t))
t = (1, 5, )
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(type(v))

a, b, c = v
print(a, b, c)