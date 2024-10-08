# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
#
# if a > b and a > c:
#     if b + c > a:
#         print("Треугольник с такими сторонами существует!1")
# elif b > a and b > c:
#     if a + c > b:
#         print("Треугольник с такими сторонами существует!2")
# elif c > a and c > b:
#     if a + b > c:
#         print("Треугольник с такими сторонами существует!3")
# else:
#     print("Такой треугольник не может существовать")


a = int(input("Введите первую сторону треугольника: "))
b = int(input("Введите вторую сторону треугольника: "))
c = int(input("Введите третью сторону треугольника: "))
result1 = a > b and a > c and ((b + c) > a)
result2 = b > a and b > c and ((a + c) > b)
result3 = c > a and c > b and ((a + b) > c)

# print(result1)
# print(result2)
# print(result3)

if result1 == True or result2 == True or result3 == True:
    print("Треугольник с такими сторонами существует!")
else:
    print("Такой треугольник не может существовать")



