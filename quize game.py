def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Wrong! Correct answer is:", answer)
        return 0


def quiz_game():
    score = 0

    score += ask_question("1. What is the capital of India?", "Delhi")
    score += ask_question("2. 5 + 3 = ?", "8")
    score += ask_question("3. Which language is used for Python?", "English")

    print("Your total score is:", score)


# Run the game
quiz_game()