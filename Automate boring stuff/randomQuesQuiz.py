import os, random
from pathlib import Path
os.system('cls')

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany','North Carolina': 'Raleigh', 
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
   'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
   'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

folderpath = 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/AutomateBoringStuff/tests'
for quizNum in range(35):
    quizfilepath = 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/AutomateBoringStuff/tests/' + f'capitalquiz{quizNum +1}.txt'
    answerFilePath = 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/AutomateBoringStuff/tests/' + f'capitalquiz_answers{quizNum +1}.txt'
    quizFile = open(quizfilepath, 'w')
    answerFile = open(answerFilePath, 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    for quesNum in range(50):
        correctAnswer = capitals[states[quesNum]]
        wrongAnswers =  list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'{quesNum + 1}. what is the capital of {states[quesNum]}?\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. {answerOptions[i]} \n")
        quizFile.write('\n')
        answerFile.write(f"{quesNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerFile.close()