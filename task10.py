# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".

N = int(input())
M = 0
m = 999999
for l in range(N):
    i = int(input())
    if i != 0:
        e = 1
        for c in range(2, int(i ** 0.5) + 1):
            if i % c == 0:
                e = 0
                break
            else:
                e = 1
        if e == 1:
            if i > M:
                M = i
            if i < m:
                m = i
if M!=m:
    print(M,m)
elif M==m:
    print(M)
elif M ==1 and m ==999999:
    print("no")
