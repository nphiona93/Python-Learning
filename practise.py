# write a program to tell the user if the number entered is divisible by 3
number = input("Enter a number : ")


print (int(number))

if int(number) == number:
    if (int(number) % 3) == 0:
        print (number + " is divisible by 3")

    else:
        print (number + " not divisible by 3")

else:
    print("Enter an integer")





