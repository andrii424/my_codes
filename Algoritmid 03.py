def bubble_sort(array):
    # Проходим по массиву
    for i in range(len(array)-1):
        # В каждой итерации сравниваем элементы и перемещаем больший элемент вправо
        for j in range(len(array)-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    # Выводим отсортированный массив
    print(array)

arr = [1, 2, 3, 4, 1, 2, 10, 15, 2, 3, 4]
bubble_sort(arr)