
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

start = True
stop = True
quit = False
while(True):
    command = input()

    if command == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "start":
        print("Car is running...")
        start = False
    elif command == "stop":
        print("Car has stopped")
        stop = False
    elif command == "quit":
        print("exiting.....")
        break
    elif command != "help":
        print("I don't understand that...")

