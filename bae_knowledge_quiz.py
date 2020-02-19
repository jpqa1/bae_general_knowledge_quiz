# BAE General Knowledge Quiz: A python programme to demonstrate my knowledge
# of the python programming language and BAE Systems.

# Variables
num_of_q = 10
result = 0
correct_q = []
num_correct_q = len(correct_q)
percentage_correct = len(correct_q) / num_of_q * 100
incorrect_q = []
take_quiz = 'yes'

# Title of quiz and user info collected
print('BAE Systems: General Knowledge Quiz:')
print()
name = input('Please enter your first name? ')
print()
print(input(name + ', Welcome to the BAE General Knowledge Quiz. The pass mark for this quiz is 50%. Hit enter to start? >>>>> '))
print()

while take_quiz == 'yes':
    # Question 01
    print('----- QUESTION 01 -----')
    print()
    q01 = 'What year was BAE systems founded?'
    q01_options = '1. 1999, 2. 2007, 3. 1980:'
    print(q01)
    print()
    print(q01_options)
    print()
    q01_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 01 Conditional Statement
    if q01_user_answer == 1:
        print('CORRECT!! BAE Systems was founded on November 30th 1999 through a merger between British Aerospace and Marconi Electronic Systems.')
        print()
        print()
        result += 1
        correct_q.append('Question 01')
    else:
        incorrect_q.append('Question 01')
        print('INCORRECT! BAE Systems was founded November 30th 1999')
        print()
        print()

    print()
    # End of question 01

    # Question 02
    print('----- QUESTION 02 -----')
    print()
    q02 = 'Who is currently the CEO of BAE Systems?'
    q02_options = '1. Julian Cracknell, 2. Dr. Charles Woodburn, 3. Chris Boardman:'
    print(q02)
    print()
    print(q02_options)
    print()
    q02_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 02 Conditional Statement
    if q02_user_answer == 2:
        print('CORRECT!! Dr. Charles Woodburn is the current CEO of BAE Systems, Julian Cracknell is the Managing Director of BAEs subsidiary company BAE Applied Intelligence and Chris Boardman is the group Managing Director of the Air division.')
        print()
        print()
        result += 1
        correct_q.append('Question 02')
    else:
        incorrect_q.append('Question 02')
        print('INCORRECT! The correct answer is Dr. Charles Woodburn.')
        print()
        print()

    print()
    # End of question 02

    # Question 03
    print('----- QUESTION 03 -----')
    print()
    q03 = 'In 2018, how much money did BAE contribute to the UK Gross Domestic Product?'
    q03_options = '1. £9.3 Million, 2. £90 Million, 3. £9.3 Billion:'
    print(q03)
    print()
    print(q03_options)
    print()
    q03_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 03 Conditional Statement
    if q03_user_answer == 3:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 03')
    else:
        incorrect_q.append('Question 03')
        print('INCORRECT! The correct answer is £9.3 Billion.')
        print()
        print()

    print()
    # End of question 03

    # Question 04
    print('----- QUESTION 04 -----')
    print()
    q04 = 'What class of next generation nuclear detterant submarine will eventually replace the Vanguard class of submarine? '
    q04_options = '1. Subzero, 2. Dreadnought, 3. Hunter  :'
    print(q04)
    print()
    print(q04_options)
    print()
    q04_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 04 Conditional Statement
    if q04_user_answer == 2:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 04')
    else:
        incorrect_q.append('Question 04')
        print('INCORRECT! The correct answer is Dreadnought.')
        print()
        print()

    print()
    # End of question 04

    # Question 05
    print('----- QUESTION 05 -----')
    print()
    q05 = 'Which foundation does BAE Applied Intelligence support in order to combat illegal content online? '
    q05_options = '1. Web Watch Foundation, 2. Illegal Content Watch Foundation, 3. Internet Watch Foundation  :'
    print(q05)
    print()
    print(q05_options)
    print()
    q05_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 05 Conditional Statement
    if q05_user_answer == 3:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 05')
    else:
        incorrect_q.append('Question 05')
        print('INCORRECT! The correct answer is Internet Watch Foundation.')
        print()
        print()

    print()
    # End of question 05

    # Question 06
    print('----- QUESTION 06 -----')
    print()
    q06 = "In 2014 BAE supported the National Crime Agency's CEOP command with an operation that lead to the arrest of 660 suspected paedophiles and the safeguarding of over 400 children across the UK. What was this operation titled?"
    q06_options = '1. Operation Notarise, 2. Operation Safeguard, 3. Operation Cyber Protect :'
    print(q06)
    print()
    print(q06_options)
    print()
    q06_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 06 Conditional Statement
    if q06_user_answer == 1:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 06')
    else:
        incorrect_q.append('Question 06')
        print('INCORRECT! The correct answer is Operation Notarise.')
        print()
        print()

    print()
    # End of question 06

    # Question 07
    print('----- QUESTION 07 -----')
    print()
    q07 = "Approximatley how many people work for BAE worldwide?"
    q07_options = '1. 75,000, 2. 85,000, 3. 82,500 :'
    print(q07)
    print()
    print(q07_options)
    print()
    q07_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 07 Conditional Statement
    if q07_user_answer == 2:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 07')
    else:
        incorrect_q.append('Question 07')
        print('INCORRECT! The correct answer is 85,000.')
        print()
        print()

    print()
    # End of question 07

    # Question 08
    print('----- QUESTION 08 -----')
    print()
    q08 = "Which body have certified BAE Systems to provide global penetration testing services?"
    q08_options = '1. CREST, 2. CESG, 3. Management Consulting Association (MCA) :'
    print(q08)
    print()
    print(q08_options)
    print()
    q08_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 08 Conditional Statement
    if q08_user_answer == 1:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 08')
    else:
        incorrect_q.append('Question 08')
        print('INCORRECT! The correct answer is CREST.')
        print()
        print()

    print()
    # End of question 08

    # Question 09
    print('----- QUESTION 09 -----')
    print()
    q09 = "This year (2020) BAE will recruit a record number of apprentices. Approximatley how many in total?"
    q09_options = '1. 2000, 2. 700, 3. 800 :'
    print(q09)
    print()
    print(q09_options)
    print()
    q09_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 09 Conditional Statement
    if q09_user_answer == 3:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 09')
    else:
        incorrect_q.append('Question 09')
        print('INCORRECT! The correct answer is 800.')
        print()
        print()

    print()
    # End of question 09

    # Question 10
    print('----- QUESTION 10 -----')
    print()
    q10 = "Approximatley how much did BAE systems invest in education, skills and early careers activities in the UK in 2018?"
    q10_options = '1. £25 Million. , 2. £50 Million, 3. £100 Million :' 
    print(q10)
    print()
    print(q10_options)
    print()
    q10_user_answer = int(input('Please answer the question by typing 1, 2 or 3: >>>>> '))
    print()

    # Question 10 Conditional Statement
    if q10_user_answer == 3:
        print('CORRECT!')
        print()
        print()
        result += 1
        correct_q.append('Question 10')
    else:
        incorrect_q.append('Question 10')
        print('INCORRECT! The correct answer is 800.')
        print()
        print()

    print()
    # End of question 10

    # Calculates the average result of user expressed as a percentage
    percentage_correct = round(len(correct_q) / num_of_q * 100)
    print('Your score: ', percentage_correct, '%')
    print()

    # Conditional statement to determine if the user has passed the quiz.
    if percentage_correct >= 50:
        print('Well Done',name,'! You passed.')
        print()
    else:
        print('Unfortunatley you have failed. Please try again.')
        print()
        
    # Prints the list of questions answered correctly and incorrectly    
    print('You answered the following questions correctly:')
    print(correct_q)
    print()
    print('You answered the following questions incorrectly:')
    print(incorrect_q)
    print()

    
    # Reset the Variables
    correct_q = []
    incorrect_q = []
    result = 0

    # Gives the user the option of re-sitting the quiz
    take_quiz = input('Do you want to try again? (Please type yes or no) ')
    print()
    print()
    

else:
    print()
    print('Thank you for taking the quiz. Goodbye.')








