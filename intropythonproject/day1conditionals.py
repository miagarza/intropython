#CONDITIONALS
#You dont always want to run every line of code you have
#Code only runs when a given condition was true
#if statement: If [Condition], then [Code]

num1 = 10
num3= 5
num2=int(input("Enter a number: "))

#uses > greater than and < less than, and add = to make it "equals"
# == means equal to while = is just checking if it is true
# ex. 5=5 making the variable, but its not true so you need ==

if(num2 > num1):
    print("This number is greater than 10!")
#elif is second condition, you can have as many elif as you want
elif(num2 > num3):
    print("This number is greater than 5")
elif (num2 > 1):
    print("This number is greater than 1")
else:
    print("This number is negative")
