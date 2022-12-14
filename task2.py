# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
#not (x or y or z) == not x and not y and not z

for x in range (10):
        for y in range (10):
            for z in range (10):
                print(not (x or y or z) == (not x and not y and not z))
                print (x, y, z)
