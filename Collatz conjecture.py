end = False
number = int(input("Give me a number \n"))
original_number = number
counter = 0
while not end:
    print(number)
    if number == 1:
        end = True
    elif number % 2 == 0:
        number = number / 2

    elif not number % 2 == 0:
        number *= 3
        number += 1
    counter += 1

print(f"It took {original_number}, {counter} steps to reach 1!")
