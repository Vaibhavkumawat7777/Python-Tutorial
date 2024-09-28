import time
import this

h = int(time.strftime("%H"))
print()
print()
print()
print("This is K.B.C. where I'll ask 10 questions to you and you have 4 options to answer the questions.")
print('You can quit the game by entering "Quit"')

print("To answer the question you only have to enter the option LETTER in the text box")
print("For Ex.  Answer of question: A")
name = input("Enter your name:")
if(name == "Quit" or name == "quit"):
    exit()


if(h >= 7 and h< 12):
    print("Good Morning", name)
elif(h >= 12 and h < 18):
    print("Good Afternoon", name)
elif(h >=18 or h <7):
    print("Good Night", name)

print("So,",name,", Are You Ready!!!")

questions = [
    "What is the capital of France?",
    'Who wrote the play "Romeo and Juliet"?',
    'Which planet is known as the "Red Planet"?',
    'What is the chemical symbol for water?',
    'Who painted the "Mona Lisa"?',
    'What is the largest mammal on Earth?',
    'Which gas do plants use for photosynthesis?',
    'Who is the author of "To Kill a Mockingbird"?',
    'What is the currency of Japan?',
    'Which scientist formulated the theory of relativity?',
    "Who is the current Railway Minister of India?",
    "Which god is also known as ‘Gauri Nandan’?",
    "What does not grow on a tree according to a popular Hindi saying?",
    "Which city is known as the Pink City in India?",
    "Who wrote India’s National Anthem?",
    "Which of the following companies was originally started as a loom manufacturing unit in 1909?",
    "In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?"
    ]


optionA = [
    'Paris',
    'Charles Dickens',
    'Venus',
    'H2O',
    'Vincent van Gogh',
    'Elephant',
    'Oxygen',
    'J.K. Rowling',
    'Yen',
    'Isaac Newton',
    " Mamta Banarjee",
    "Agni",
    "Money",
    "Bangalore",
    "Rabindranath Tagore",
    "Suzuki",
    "Udit Narayan"
    ]

optionB = [
    'London',
    'William Shakespeare',
    'Mars',
    'CO2',
    'Pablo Picasso',
    'Blue whale',
    'Nitrogen',
    'Harper Lee',
    'Euro',
    'Albert Einstein',
    "Ram Vilash",
    "Indra",
    "Flowers",
    "Mysore",
    "Lal Bahadur Shastri",
    "CEAT",
    "A. R. Rahman"
    ]

optionC = [
    'Berlin',
    'Jane Austen',
    'Jupiter',
    'O2',
    'Leonardo da Vinci',
    'Giraffe',
    'Carbon dioxide',
    'George Orwell',
    'Dollar',
    'Galileo Galilei',
    "Ashwini Vaishnaw",
    " Hanuman",
    "Leaves",
    "Jaipur",
    "Chetan Bhagat",
    "Honda",
    "Lata Mangeshkar"
    ]

optionD = [
    'Rome',
    'Mark Twain',
    'Saturn',
    'CH4',
    'Michelangelo',
    'Rhinoceros',
    'Hydrogen',
    'F. Scott Fitzgerald',
    'Pound',
    'Nikola Tesla',
    "Piyush Goya",
    "Ganesha",
    "Fruits",
    "Kochi",
    "Kuvempu",
    "Mercedes",
    "Raj Burman"
    ]

correctAnswers = [
    "A",
    "B",
    'B',
    'A',
    'C',
    'B',
    'C',
    'B',
    'A',
    'B',
    "C",
    "D",
    "A",
    "C",
    "A",
    "A",
    "B"
]

levels = [
    "₹0/-",
    "₹10,000/-",
    "₹3,20,000/-",
    "₹75,00,000/-",
    "₹7.5 Crore/-"
]
level = 1
price = [
    "₹1,000/-",
    "₹2,000/-",
    "₹3,000/-",
    "₹5,000/-",
    "₹10,000/-",
    "₹20,000/-",
    "₹40,000/-",
    "₹80,000/-",
    "₹1,60,000/-",
    "3,20,000/-",
    "6,40,000/-",
    "₹12,50,000/-",
    "₹25,00,000/-",
    "₹50,00,000",
    "₹75,00,000/-",
    "₹1 Crore/-",
    "₹7.5 Crore/-"
]

index = 0   

while(index < 17):
    if index == 5:
        level += 1
    elif index == 10:
        level += 1
    elif index == 15:
        level += 1
    print(f"Level: {level}")
    print(index + 1, ") ", questions[index])
    print("- A) ", optionA[index])
    print("- B) ", optionB[index])
    print("- C) ", optionC[index])
    print("- D) ", optionD[index])
    answer = input("Enter Correct Option LETTER: ")
    if(answer.capitalize() == correctAnswers[index]):
        print("Correct Answer!!!")
        print(f"You won {price[index]}")
        print()
        print()
    else:
        print("Wrong Answer!!!")
        print(f"You won {levels[level-1]}")
        break
    index += 1
    if(answer == "Quit" or answer == "quit"):
        break