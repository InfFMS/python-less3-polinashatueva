# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a = int(input())
b=0
c=0
while a != 0:
    if a >9 and a <100:
        b += 1
    else:
        c += 1
    a = int(input())
print(b,c)



