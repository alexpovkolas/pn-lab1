def fizzbuzz(start, end):
    start_index = start if start % 2 == 1 else start + 1
    for x in range(start_index, end, 2):
        if x % 3 == 0 and x % 7 == 0:
            print("FizzBuzz", end=' ')
        elif x % 3 == 0:
            print("Fizz", end=' ')
        elif x % 7 == 0:
            print("Buzz", end=' ')
        else:
            print(x, end=' ')


fizzbuzz(1, 101)
