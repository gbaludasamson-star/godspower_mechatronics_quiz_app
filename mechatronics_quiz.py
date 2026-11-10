# Mechatronics Quiz App
# A short multiple-choice quiz with score, grade and review of mistakes

# Lists that store the quiz content
questions = [
    "Which device converts electrical energy into motion?",
    "What does a sensor do?",
    "What does PLC stand for?",
    "Which law says V = I x R?",
    "Which component works as an electrically controlled switch?",
    "What is the unit of electrical resistance?",
]

options = [
    ["Motor", "Sensor", "Capacitor", "Diode"],
    ["Moves a part", "Detects a change", "Stores energy", "Cuts metal"],
    ["Power Line Circuit", "Programmable Logic Controller",
     "Primary Load Component", "Parallel Logic Current"],
    ["Newton's law", "Ohm's law", "Faraday's law", "Hooke's law"],
    ["Relay", "Resistor", "Capacitor", "Inductor"],
    ["Volt", "Ampere", "Ohm", "Watt"],
]

# Number (1-4) of the correct option for each question
answers = [1, 2, 2, 2, 1, 3]


def get_choice():
    """Keep asking until the user types a number from 1 to 4, then return it."""
    while True:
        try:
            choice = int(input("Your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("That is not a number. Please type 1, 2, 3 or 4.")


def get_grade(percent):
    """Return a message based on the final percentage."""
    if percent >= 80:
        return "Excellent! You think like an engineer."
    elif percent >= 50:
        return "Good effort. Keep practising."
    else:
        return "Keep studying, you will get better."


# ---- Main program ----
score = 0
missed = []  # my twist: remember the questions the user got wrong

print("=== Mechatronics Quiz ===")

for i in range(len(questions)):
    print("\nQuestion", i + 1, ":", questions[i])
    for number, option in enumerate(options[i], start=1):
        print(number, ".", option)

    choice = get_choice()

    if choice == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong.")
        missed.append(i)

percent = score / len(questions) * 100
print("\nYou scored", score, "out of", len(questions), "(", round(percent), "% )")
print(get_grade(percent))

# My twist: review the missed questions with the right answers
if len(missed) > 0:
    print("\n--- Review of questions you missed ---")
    for i in missed:
        print(questions[i], "->", options[i][answers[i] - 1])