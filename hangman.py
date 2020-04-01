import random


#Funktion die prüft ob der eingegebene Buchstabe im Wort vorhanden ist
def check_letter(wd,wl,array):

 wrong = 0
 strike = 0
 counter = 0
 guess_array = array

 while strike < 11:
    guess = input("Rate einen Buchstaben: ")
    for i in wd:
        if guess == i:
            counter = counter + 1
            guess_array.insert(counter,i)
            del guess_array[counter - 1]

        else:
            wrong = wrong + 1
            counter = counter + 1

    if wrong == wl:
        strike = strike + 1
        print("Incorrect!")
        print("Wrong Guesses: " + str(strike))
        print(guess_array)
        wrong = 0
        counter = 0
    else:
        print("Correct!")
        print(guess_array)
        wrong = 0
        counter = 0
    if "-" not in guess_array:
        return print ("Congratulations, you guessed the word!")




#Liste die alle verfügbaren Wörter enthält
wordlist = ['feuerwehr', 'polizei', 'rettungswagen']
#Funktion um ein zufälliges Wort aus der Liste auszuwählen
word = random.choice(wordlist)
#Länge des aktuellen Wortes
wordlength = len(word)
#Erstellen des Arrays, welches später die richtig geratenen Buchstaben enthält
guess_array = []
for i in word:
    guess_array.append("-")



print("Das gesuchte Wort hat " + str(wordlength) + " Buchstaben")

check_letter(word,wordlength,guess_array)