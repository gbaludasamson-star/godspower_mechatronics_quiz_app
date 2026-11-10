# Mechatronics Quiz App

## What it does
A short multiple-choice quiz on mechatronics topics, written in Python. It asks six questions, checks each answer, keeps the score, and gives a final percentage with a grade message. At the end it shows the questions you missed and their correct answers.

## How to run it
Install Python 3, then run: python mechatronics_quiz.py

## Sample output
```
=== Mechatronics Quiz ===

Question 1 : Which device converts electrical energy into motion?
1 . Motor
2 . Sensor
3 . Capacitor
4 . Diode
Your answer (1-4): a
That is not a number. Please type 1, 2, 3 or 4.
Your answer (1-4): 1
Correct!

You scored 5 out of 6 ( 83 % )
Excellent! You think like an engineer.

--- Review of questions you missed ---
What does PLC stand for? -> Programmable Logic Controller
```

## My own twist
At the end of the quiz, the program shows a review of the questions I got wrong, together with the correct answers, so the user can learn from their mistakes.

## What I learned
I learned how to store questions, options and answers in lists and loop through them. I also learned to check user input with try/except so the program does not crash when a letter is typed instead of a number.

## Author
Gbaluda Godspower Oluwatosin, ND2 Mechatronics Engineering, YabaTech.
