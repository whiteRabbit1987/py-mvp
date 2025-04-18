# Quiz game

questions = ("How many continents are there on Earth?: ",
             "Which mammal can fly?: ",
             "What is the primary gas plants use for photosynthesis?: ",
             "How many legs does a spider have?: ",
             "Which planet is known as the Red Planet?: ")

options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Bat", "B. Squirrel", "C. Monkey", "D. Lemur"),
           ("A. Carbon Dioxide", "B. Nitrogen", "C. Oxygen", "D. Hydrogen"),
           ("A. 6", "B. 7", "C. 8", "D. 9"),
           ("A. Jupiter", "B. Mars", "C. Mercury", "D. Venus"))

answers = ("C", "A", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print('-------------------------')
print('        RESULT           ')
print('-------------------------')

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")