# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

print ('Введите число N')
N = int (input ())
Max = 2
i = 1
while Max <= N:
    print (Max, end=' ')
    Max = 2 ** i
    # if Max >=N: 
    #     break
        
    i+=1
    
    

  


