'''
Exercise 3: List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
'''

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove('Banana')
print(basket)
basket.remove('Blueberries')
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(0, 'Apples')
print(basket)
print(basket.count('Apples'))
basket.clear()
print(basket)