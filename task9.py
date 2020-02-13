#Напишите код, который посчитает количество чисел от 100 до 999, в которых каждая цифра числа отличается от других цифр не менее, чем на 3 (например: 147, 159, 629, 408 и т.п.)
#Python

list = []

for i in range(100, 1000):
    str = i.__str__()
    a, b, c = str
    if abs(int(a) - int(b)) >= 3 or abs(int(b) - int(a) >= 3):
        if abs(int(b) - int(c)) >= 3 or abs(int(b) - int(c)) >= 3:
            if abs(int(a) - int(c)) >= 3 or abs(int(c) - int(a) >= 3):
                list.append(i)

print(list)
