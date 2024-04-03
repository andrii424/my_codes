def BubbleSort(array):
    # Проходим по массиву
    for i in range(len(array)):
        swapped = False  # Флаг, чтобы отслеживать, были ли обмены на текущей итерации
        # Проходим по элементам массива до i-го (уже отсортированной части)
        for j in range(len(array) - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True  # Устанавливаем флаг обмена
        # Если на текущей итерации не было обменов, значит массив уже отсортирован
        if not swapped:
            break
        print("1")
        print(array)
    
    # Выводим отсортированный массив
    print("Отсортированный массив:")
    print(array)

arr = [1,2,3,4,1,2,10,15,2,3,4]
BubbleSort(arr)
