text = "Hello,Python!"
print (text [0]) #Выведет первый символ
print (text [0:5]) #Выведет первую строку text от 0 символа до 5
print (text [4:10]) #Выведет строку от 4 смивола до 10(включая 4,исключая 10)
print (text [0:14]) #Выведет всю строку
print (text [7:]) #Выведет строку с 7 символа до конца 
print (text [:5]) #Выведет строку с начала до 5 символ
print (text [ : ]) #Выведет всю строку
print (text [-1]) #Выводит последний символ 
print (text [-1:-14]) #Не сработает, выведет пустую строку 
print (text [: : 2]) #Третий аргумент-шаг. Выведет второй символ 
print (text [: : -1]) #Шаг отрицательный.Выведет фразу наоборот
print (text + "Nice to code you") #Выведет новую строку
print (text [-1] *10) #Выведет 10 восклицательных знаков