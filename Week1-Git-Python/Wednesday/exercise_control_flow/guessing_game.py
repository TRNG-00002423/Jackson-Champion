import random

answer = random.randint(1, 100)
guess_count = 0
did_win = False


while guess_count < 7:
    print("Guess a number 1 - 100: ")
    user_guess = int(input())
    guess_count += 1

    if user_guess > answer:
        print(f"{user_guess} is Too high! you get {7 - guess_count} more attempt(s).")
        continue
    
    elif user_guess < answer:
        print(f"{user_guess} is Too low! you get {7 - guess_count} more attempt(s).")
        continue
    
    else:
        print(f"Congratulations! You guessed the correct number: {answer}")
        did_win = True
        break
    
if not did_win:
    print(f"Sorry. You've ran out of attempts. The answer was {answer}.")  


