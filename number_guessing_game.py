import random
print("Hey!, Welcome to number precision game made by BizonTR. Please choose a difficulty for continue.")
print("Easy (Numbers range from 1 to 100) For Easy: write 1")
print("Normal (Numbers range from 1 to 150) For Normal: write 2")
print("Hard (Numbers range from 1 to 200) For Hard: write 3")
difficulty=int(input("Please write for any difficulty: "))
while not (difficulty==1 or difficulty==2 or difficulty==3):
    print("Please enter a correct difficulty.")
    difficulty=int(input("Please write for any difficulty: "))
if difficulty==1:
    number=random.randint(1,101)
    print("Game has started. Computer chose a number between 1 and 100. You have 10 lifes for find it. Write your guess and see what you need to do.")
elif difficulty==2:
    number=random.randint(1,151)
    print("Game has started. Computer chose a number between 1 and 150. You have 10 lifes for find it. Write your guess and see what you need to do.")
elif difficulty==3:
    number=random.randint(1,201)
    print("Game has started. Computer chose a number between 1 and 200. You have 10 lifes for find it. Write your guess and see what you need to do.")
life=10
while life>0:
    predicted_number=int(input("Write your guess: "))
    if predicted_number<number:
        life-=1
        print("Please write a larger number. Remaining lifes:" + str(life))
    if predicted_number>number:
        life-=1
        print("Please write a smaller number. Remaining lifes:" + str(life))
    if predicted_number==number:
        print("Congratulations! You have found the correct number. Your remaining lifes were: " + str(life))
        break
    elif life==0:
        print("You lost. Correct number was: " + str(number) + " " + "Good luck for the next one!")
        break
