x = int(input("Enter an integer: "))
ans = 0

while ans ** 3 < x:
    ans += 1
if ans ** 3 != x:
    print (str(x) + " is not a perfect cube ")
else:
    print (ans, " is the cube root of ", x)
