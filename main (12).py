#coding: utf-8
#Задача 1
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a>b:
    maximus= a
    minimus= b
else:
    maximus= b
    minimus= a
print("Ответ:")
print("Максимальное число:",maximus)
print("Минимальное число:",minimus)
#Задача 2
c=int(input("Введите сторону квадрата: "))
r=int(input("Введите радиус круга: "))
d = r*2
if c <= d:
    print("Круг впишется в квадрат")
else:
    print("Круг не впишется в квадрат")
#Задача 3
x=int(input("Введите первое число: "))
if x<0:
    y=x*x
else:
    y=1/x*x
print("Ответ:",y)
#Задача 4
a=int(input("Введите сторону квадрата: "))
r=int(input("Введите радиус круга: "))
if 2*b >=r:
    print("Квадрат впишется в круг")
else:
     print("Квадрат не впишется в круг")
#Задача 5
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a > b:
    print("Наибольшее число:", a)
elif b > a:
    print("Наибольшее число", b)
else:
    print("Числа равны")
#Задача 6
x=int(input("Введите первое число: "))
if x<=0:
    y=x*x
else:
    y=1/x*x
print("Ответ:",y)
#Задача 7
    