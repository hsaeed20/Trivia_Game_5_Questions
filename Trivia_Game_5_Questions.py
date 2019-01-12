#Ask the user to answer 5 questions to a trivia game and let them know how many they got right. Allow the user if he/she would like to play again
import requests
import itertools 
from random import choice

while "Yes":
    right_answers = 0 #used to see how many answers the user got right
    
    url = 'https://opentdb.com/api.php?amount=10'
    res = requests.get(url) #gets the information from url
    
    data = res.json()
    question1 = data['results'][0]
    question2 = data['results'][1]
    question3 = data['results'][2]
    question4 = data['results'][3]
    question5 = data['results'][4]
    
    #Question 1
    q1 = question1['question']
    correct_answer1 = question1['correct_answer']
    incorrect_answers1 = question1['incorrect_answers']


    print("Question 1\n")
    print(q1,'\n')

    for i in incorrect_answers1:
        print(i)
    print(correct_answer1)

    choice1 = input("\nWhat is your answer: ").strip().title() #title was done to make the first letter auto-capitalized since all answer choices are done as such

    if choice1 == correct_answer1:
        print("Correct! The answer is", correct_answer1)
        right_answers = right_answers + 1
    
    else:
        print("Incorrect! The answer is", correct_answer1)

    #Question 2
    print("Question 2\n")

    q2 = question2['question']
    correct_answer2 = question2['correct_answer']
    incorrect_answers2 = question2['incorrect_answers']

    print(q2,'\n')
    
    for i in incorrect_answers2:
        print(i)
    print(correct_answer2)

    choice2 = input("\nWhat is your answer: ").strip().title()
    
    if choice2 == correct_answer1:
        print("Correct! The answer is", correct_answer2)
        right_answers = right_answers + 1
    
    else:
        print("Incorrect! The answer is", correct_answer2)
    
    #Question 3
    print("Question 3\n")

    q3 = question3['question']
    correct_answer3 = question3['correct_answer']
    incorrect_answers3 = question3['incorrect_answers']
    
    print(q3,'\n')
    
    for i in incorrect_answers3:
        print(i)
    print(correct_answer3)

    choice3 = input("\nWhat is your answer: ").strip().title()

    if choice3 == correct_answer3:
        print("Correct! The answer is", correct_answer3)
        right_answers = right_answers + 1
    
    else:
        print("Incorrect! The answer is", correct_answer3)


    #Question 4
    print("Question 4\n")

    q4 = question4['question']
    correct_answer4 = question4['correct_answer']
    incorrect_answers4 = question4['incorrect_answers']

    print(q4,'\n')

    for i in incorrect_answers4:
        print(i)
    print(correct_answer4)

    choice4 = input("\nWhat is your answer: ").strip().title()

    if choice4 == correct_answer1:
        print("Correct! The answer is", correct_answer4)
        right_answers = right_answers + 1
    
    else:
        print("Incorrect! The answer is", correct_answer4)


    #Question 5
    print("Question 5\n")

    q5 = question5['question']
    correct_answer5 = question5['correct_answer']
    incorrect_answers5 = question5['incorrect_answers']

    print(q5,'\n')

    for i in incorrect_answers5:
        print(i)
    print(correct_answer5)

    choice5 = input("\nWhat is your answer: ").strip().title()

    if choice5 == correct_answer5:
        print("Correct! The answer is", correct_answer5)
        right_answers = right_answers + 1
    
    else:
        print("Incorrect! The answer is", correct_answer5)
    
    if right_answers == 5:
        print("NICE WORK!")
        print("5/5")
    else:
        print("The amount of correct answers you've recieved:", right_answers, "/5")
        
    #Used to decide if the game is over or not    
    decision = input("Would you like to play again (Yes/No): ").strip().title()
    
    if decision == "No": 
        print("Thank you for playing! We hope to see you again!")
        break;
    
    
