#I was watching a video by Veritasium about the Collatz Conjecture and thought it would be fun to make my own program for it! 
#If you come across this and see I've made a mistake please contact me :D
end = False
number = int(input("Give me a number \n"))
counter = 0
while not end:

    if number % 2 == 0:
        number = number / 2

    if number == 1:
        end = True

    if not number % 2 == 0:
        number *= 3
        number += 1
    counter += 1

print(counter)
