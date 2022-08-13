nameArray = [0,1,2,3,4]
for num in nameArray:
    print("Phiona " + str(num))

print(len('nameArray'))

# # # Write a program that gives the sum of all numbers in the Array/List
total = 0
for number in nameArray:
    print( total, number)
    total =number+ total
    
print(total)

# # #Exercise 1

# # # 1. Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
number = input("Enter a number of your choice")
total = 0
 
for num  in range(10,int(number)):
    print(num, total)
    total = num + total
print(total)

# # 2. Display numbers from -10 to -1 using for Loop 

for number in reversed (range(-10,0)):
    print(number)

# #3. Find the factorial of a given number

number = input("Enter any number")

total = 1

for num in range (1, int(number) +1):
    print(num, total)
    total = num * total
    print( total)

print(total)

# #4. Use loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list = []
counter = 0
for number in my_list:
    if (counter % 2) != 0:
        new_list.append(number)
    counter = counter + 1

print(new_list)

for num1 in new_list:
    print(num1)

# #5. Write the program to count the number of e in the word coffee
name = "coffee"
counter = 0
for num in name:
    if num == "e":
        counter = counter + 1
   # print (len(name))

print (counter)

#6. Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000. 
#i.e.: if the value is 1500, 500 should be added to the new list.


my_list = [1200, 1400, 300, 7000, 1500, 500]
new_list = []

for num in my_list:
    if num > 1000:
        new_list.append(num -1000)
print(new_list)

#7. Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
new_list = []

for num1 in lst1:
    new_list.append(type(num1))
print (new_list)