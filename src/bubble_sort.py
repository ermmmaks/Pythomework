def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temporary = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temporary
                swapped = True
        if not swapped:
            return arr

len_arr = int(input("Введите длину массива: "))
user_arr = []

for count in range(len_arr):
    user_number = int(input(f"Число номер {count + 1}: "))
    user_arr.append(user_number)

print("Сортировка выполнена!")
print(bubble_sort(user_arr) )