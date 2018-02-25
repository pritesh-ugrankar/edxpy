num = 100
print("outside the while loop")
while not False:
    print("just below the while loop")
    if num < 0:
        print("just below the if condition")
        break
print('num is: ' + str(num))
