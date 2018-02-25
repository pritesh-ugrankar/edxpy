x = int(input("Enter an integer: "))
ans = 0

while ans ** 3 < x:
    ans += 1
if ans ** 3 == x:
    print (ans, " is the cube root of ", x)
else:
    print (x, " is not a perfect cube")
