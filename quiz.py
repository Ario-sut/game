print('Welcome to the Quiz Game by Fit')
ans = input('Are you ready to play (y/n) : ')

score = 0
question = 5

if ans.lower() == 'yes' or ans.lower() == 'y':
    #First question
    print('1. what is the capital city of Singapore')
    print('a. Singapore')
    print('b. Hanoi')
    print('c. Ho Chi Minh')
    print('d. Bangkok')
    ans = input('Please choose your answer (pick the letter): ')
    if ans.lower() == 'a':
        score +=1
        print('Correct')
    else:
        print('incorrect')
    print()

    #Second Question
    print('How long is the presidents period of reign in Indonesia : ')
    ans = int(input('Your answer (in number) : '))
    if ans == 5:
        score +=1
        print('Correct')
    else:
        print('incorrect')
    print()

    #Third Question
    print('3. ( 343 x 343 + 343 x 257 + 257 x 257 + 343 x 257 )/( 343 + 257 )')
    print('a. 1')
    print('b. 3000')
    print('c. 600')
    print('d. 374734')
    ans = input('Please choose your answer (pick the letter): ')
    if ans.lower() == 'c':
        score +=1
        print('Correct')
    else:
        print('incorrect')
    print()

    #Fourth Question
    print('4. (2x3)!/(2x3)')
    ans = int(input('Your answer (in number) : '))
    if ans == 120:
        score +=1
        print('Correct')
    else:
        print('incorrect')
    print()

    print('5. Miranda is a programmer. She has a project that will welcome the new students in a school')
    print('   Make a program that will print "Welcome to Your First day at School" to the students in python ')
    print('   You have 3 chances only')
    
    chance = 3
    while chance > 0:
        ans = input('Make the program : ')
        if ans == 'print("Welcome to Your First day at School")' or ans == "print('Welcome to Your First day at School')":
            break
        else:
            chance-=1
            print(f'You only have {chance} left')
            print('check your mistake')
            print(ans)

if chance > 0:
    score +=1
    print('correct')
else:
    score +=0
    print('incorrect')

point = score*20
if point > 75:
    print(f"Your score is {point}")
    print('Well Done')
elif 50 < point < 75:
    print(f"Your score is {point}")
    print('Nice')
else:
    print(f"Your score is {point}")
    print('Do better next time')