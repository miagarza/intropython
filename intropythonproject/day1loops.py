#this uses a while loop to check if the input password is correct
#while loops keep on going until a condition is false

guessed= False


while not guessed:
    password = input("Enter a password: ")
    if password== "password":
        guessed=True
        print("Access Granted!")
    else:
       print("Access Denied! Try again.")



number=int(input("Enter a number"))
while number <10:
    print("This number is less than 10")
    number=number+1
#while 5 is greater is 2, print hello, it will never end bc it's true
#if we want a loop to run a certain amount of time, use for loop

