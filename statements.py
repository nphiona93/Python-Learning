print("Name Program")
name = input("What is your name?  ")
age = input("What is yoyr age? ")

gender = input("What gender are you? ")


if int(age) >= 18 :
    print( name + " is not a minor")
else:
    print( name + " is a minor")

if gender == "Female ":
    print(name + " is a Female")

elif gender == "Male":
    print(name + " is a Male")
else: 
    print(name + " is other ")
