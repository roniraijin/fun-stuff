#I was watching a video by Veritasium about the Collatz Conjecture and this my super basic attempt at making one!
#If you come across this and see I've made a mistake please contact me :D
end = False
number = int(input("Give me a number \n"))
counter = 0
while not end:
    if number == 1:
        end = True
    if number % 2 == 0:
        number = number / 2
        
    elif not number % 2 == 0:
        number *= 3
        number += 1
    counter += 1

print(counter)
