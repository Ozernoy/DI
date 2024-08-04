secret_number = int(input())
if secret_number % 3 == 0 and secret_number % 5 == 0: print('FizzBuzz')
elif secret_number % 3 == 0: print('Fizz')
elif secret_number % 5 == 0: print('Buzz')
