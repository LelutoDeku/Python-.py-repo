# i = 1;
# while i<=5 :
#     print(i)
#     i = i+1
# print("Done")

# i = 1;
# while i<=5 :
#     print('*' * i)
#     i = i+1
# print("Done")

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