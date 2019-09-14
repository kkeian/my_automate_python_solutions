def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 != 0:
        return 3 * number + 1

print('Enter a number:')

eventually_one = None
while eventually_one != 1:
    try:
        number = int(input())
        print(collatz(number))
        eventually_one = collatz(number)
    except ValueError:
        print('Enter a number genius.')
