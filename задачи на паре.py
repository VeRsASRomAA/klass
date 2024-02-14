### 1
a=int(input("Введите число"))
if a>0:
    print("Больше нуля")
#### 2
a=int(input())
if a>0:
    print(1)
else: 
    print(-1)
#### 3
a=int(input("Введите число"))
if a>5:
    print("Больше 5")
elif a<5:
    print("Меньше 5")
else:
    print("Равно 5")
########## 4 
## А)
n1=int(input("Введите число"))
n2=int(input("Введите число"))
if n1>n2: 
    n3=n1-n2
elif n1<n2: 
    n3=n1+n2
else: n3=n1
print(n3)
## Б)
h1=int(input("Введите число"))
h2=int(input("Введите число"))
h3=int(input("Введите число"))
h4=int(input("Введите число"))
if h1<h2<h3<h4:
    h5=(h1-h2)+(h3+h4)
    print(h5)
else h1<h2<h3<h4:
    h6=(h3*h4)/(h1-h2)
    print(h6)
elif h2<h1<h3<h4:
    h7=(h2+h1)-(h3*h4)
    print(h7)

if h3>h2>h1>h4:
    h8=(h4-h2)+(h3-h2)
    print(h8)
elif h1>h2>h4>h3:
    h9=(h1*h4)/(h3-h2)
    print(h9)
else h2>h1>h4>h3:
    h10=(h1-h4)/(h2+h2)
    print(h10)

if h2>h1>h4>h3:
    h11=h1-h2-h3-h4
    print(h11)
elif h1<h2<h3<h4:
    h12=h3-h2-h1-h4
    print(h12)
else h2>h1>h4>h3:
    h13=h2+h4
    print(h13)

if h2>h1>h4>h3:
    h14=h1^2+h2^5
    print(h14)
elif h1<h2<h3<h4:
    h15=h2+h3-h1
    print(h15)
else h2>h1>h4>h3:
    h16=h3-h4
    print(h16)
