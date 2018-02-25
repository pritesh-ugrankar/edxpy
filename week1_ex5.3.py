for variable in range(20):
    if variable % 4 == 0:
        print ( "In the  variable % 4 == 0: loop")
        print(variable)
    else:
        print ( "Skipping the variable  % 4 == 0: loop")

    if variable % 16 == 0:
        print ( "In the  variable % 16 == 0: loop")
        print('Foo!') 
    else: 
        print ( "Skipping the variable  % 16 == 0: loop")
