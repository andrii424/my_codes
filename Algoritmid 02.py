def sort_change(array):
    # Проходим по всем элементам массива
    for i in range(len(array)):
        # Ищем максимальный элемент, чтобы переместить его в конец
        max_val = 0
        # Идем по оставшейся части массива
        for j in range(len(array) - i):
            # Если нашли больший элемент
            if max_val < array[j]:
                # Обновляем максимальный элемент
                max_val = array[j]
                # Запоминаем его индекс
                max_index = j
        
        # Меняем местами последний элемент и максимальный
        temp = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = max_val
        array[max_index] = temp
    
    # Выводим отсортированный массив
    print(array)

# Создаем массив для сортировки
arr = [10, 3, 2, 1, 15, 30, 14, 2]
# Вызываем функцию для сортировки
sort_change(arr)
