# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

#print('Enter value N = ')
#N = int(input())
#i = 1
#value = -1/3
#while i <= N:
    #value *= -3
    #print (int(value))
    #i+=1

#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}    

print('Enter value N = ')
N=int(input())
count = 1
while count < N:
    IndexValue=3*count+1
    print(count,':',IndexValue)
    count+=1
    