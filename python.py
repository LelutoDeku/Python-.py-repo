
# while loop in python

# i = 1;
# while i<=5 :
#     print(i)
#     i = i+1
# print("Done")

#pattern in python using while

# i = 1;
# while i<=5 :
#     print('*' * i)
#     i = i+1
# print("Done")

#guess game

# secret_number = 9
# guess_count = 0;
# guess_limit = 3;
# while guess_count < guess_limit :
#     guess = int(input('Guess: '))
#     guess_count = guess_count+1
#     if guess == secret_number :
#         print('You Won!')
#         break
# else:
#     print('Try Again')

#guess game with tries

# secret_number = 9
# guess_count = 0;
# guess_limit = 3;
# while(guess_count < guess_limit):
#     guess = int(input('Guess: '))
#     guess_count = guess_count + 1
#     if guess == secret_number :
#         print('You Won!')
#         break
#     elif (guess_count == guess_limit):
#         print('You Lose!')
#         print("Want to try again?(T/F)")
#         tries = input()
#         if(tries == 'T' or tries == 't'):
#             guess_count = 0
#         else:
#             break

# Car Game

# while(True):
#     command = input("> ").lower()

#     if command == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == "start":
#         print("Car started...")
#         start = False
#     elif command == "stop":
#         print("Car has stopped")
#         stop = False
#     elif command == "quit":
#         print("exiting.....")
#         break
#     elif command != "help":
#         print("I don't understand that...")

# car game with improvements

# started = False
# while(True):
#     command = input("> ").lower()

#     if command == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == "start":
#         if started:
#             print("Car is already started...")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car has already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "quit":
#         print("exiting.....")
#         break
#     elif command != "help":
#         print("I don't understand that...")


# calculating price of items in shopping kart
# prices = [10, 20, 30, 40, 50]
# cost = 0
# for price in prices:
#     cost += price

# print(f" Total = {cost}")

# largest number in a list
# numbers = [1,23,3,64,35,56,7,8,12,10]
# largest_number = 1
# for num in numbers:
#     if num > largest_number:
#         largest_number=num
# print("Largest Number is ", largest_number)

# removing duplicates in a list
numbers = [1,2,2,3,4,5,5,4,4,6,8,8,9,9,9]
newlist=[] #new empty list
for i in range (len(numbers)):
    if numbers[i] not in newlist :
        newlist.append(numbers[i])
print ("The unique values are: ", newlist)