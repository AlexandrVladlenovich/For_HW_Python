a = int(input())
b = int(input())
c = int(input())
if a<b+c and b<a+c and c<a+b:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
if a==c==b:
        print("Треугольник равносторонний")
if a==c!=b or b==a!=c or c==b!=a:
            print("Треугольник равнобедренный")
