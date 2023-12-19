integers = {1, 2, 3, 4, 5}  #Первый набор

integers.add(7) #Добавляем новое значение в набор

second_set = {1, 3, 5, 6, 8}    #Второй набор

new_set = integers.intersection(second_set) #Находим общие числа в двух наборах и помещаем их в новый набор

new_set = list(new_set) #Конвертируем набор в список
print(new_set)  #Выводим значение списка в консоль


