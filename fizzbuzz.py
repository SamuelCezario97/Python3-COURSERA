number = int(input("Enter a number: "))


if number % 5 == 0 and number % 3 == 0:
    print("fizzbuzz")
else:
    if number % 3 == 0:
        print ("fizz")
    else:
        if number % 5 == 0:
            print("buzz")
        else:
            print("none")
