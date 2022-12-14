# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между
#  ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#AB = √(X2 - X1)^2 + (Y2 - ya)2

firstX= float (input ("Введите координату Х: "))
firstY= float (input ("Введите координату Y: "))
secondX = float (input ("Введите координату Х: "))
secondY = float (input ("Введите координату Y: "))
tempX=( secondX- firstX)**2
tempY=( secondY- firstY)**2
temp=tempX + tempY
import cmath
result= cmath.sqrt(temp)
#print(round(result, 2))
print (f"Расстояние между точками ={result }")
