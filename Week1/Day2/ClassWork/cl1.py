'''
iven this list:


list1 = [5, 10, 15, 20, 25, 50, 20]


find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


Hint : Look at the index method

Expected output:
list1 = [5, 10, 15, 200, 25, 50, 20]

'''

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    print('Postion: ', list1.index(20))
    list1[list1.index(20)] = 200
    print(list1)
else:
    print('esh beaya')