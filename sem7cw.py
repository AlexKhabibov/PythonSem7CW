# Задача 1
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде

# def transformation (a):
#     return a + 2

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = []
# for item in values:
#     new_list.append(transformation(item))
# print (new_list)


# и с лямбдой

# def transformation (a):
#     return a + 2
# transformation = lambda a: a + 2 # можно не вызыыать функцию def отдельно, а просто сослаться на условно анонимную ф-ю лямбда
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = []
# for item in values:
#     new_list.append(transformation(item))
# print (new_list)

# или можно прямо встроить в конструкцию аппенд

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = []
# for item in values:
#     new_list.append((lambda a: a + 2)(item))
# print (new_list)

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = []
# for item in values:
#     new_list.append((lambda item: item + 2)(item))
# print (new_list)

# def transformation (a):
#     return a + 2

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# map(transformation, values)

# print (list(map(transformation, values)))

# # а теперь используем лямбду
# def transformation (a):
#     return a + 2

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# map(transformation, values)

# print (list(map(lambda a: a + 2, values))) # добавляем лямбду в принт

# # Максимально упростили

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation_values = (list(map(lambda a: a + 2, values)

# print (transformation_values)



# про list comprehantion

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = []
# for a in values:
#     if a != 7:
#         new_list.append((lambda a: a + 2)(item))
# print (new_list)

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# new_list = [item for item in values if item > 4] #  что и с чем сделать ?  и откуда взять ? при каком условии(это не обязательно, но используем условие) ?
# print (new_list) # Итого получаем списко из сгенерированных элементов, которые больше 4х


# new_list = []
# for item in values:
#     new_list.append((lambda a: a + 2)(item))
# print (new_list)

# упрощаем
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print([(a + 2) for a in values if a != 7])

# Задача 2:
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# def max_pl_orb(list_1):
#     maxx = [(i[0]*i[1] if i[0] != i[1] else 0) for i in list_1] # тернарный оператор
#     return list_1[maxx.index(max(maxx))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print (*max_pl_orb(orbits))

# или через лямбду
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print (*max([(a, b) for a, b in orbits if a != b], key = lambda x: x[0] * x[1]))

# Вариант 3 от Славы:
# def max_orb(list_of_orbits):
#     s_orbits = [(x_1*x_2 if x_1 != x_2 else 0) for x_1, x_2 in list_of_orbits]
#     print(s_orbits)
#     print(max(s_orbits))
#     print(s_orbits.index(max(s_orbits)))
#     print(list_of_orbits[s_orbits.index(max(s_orbits))])
#     return list_of_orbits[s_orbits.index(max(s_orbits))]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max_orb(orbits))

# list = [(2, 4), (3, 5), (6, 1), (2, 5), (4, 4)]
# print (max(list)) # поиск максимального индекса (ищет по первому числу)
# print (max(list, key=lambda x: x[0]*x[1])) # максимальные индексы, к которым применяем условие, то есть максимальное число перемноженных индексов
# print(max([(a,b) for a,b in list if a!=b], key=lambda x: x[0]*x[1])) # и теперь исключая повторы


# Задача 3:
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) < 2

# values = [0, 2, 10, 6]

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')