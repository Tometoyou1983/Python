#English to pig latin
import os
os.system("cls")

message = input("Enter the english message to translate into Pig Latin: ")

VOWELS =('a', 'e', 'i', 'o', 'u')

pigLatin = []
for word in message.split():
    # seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    
    #seperate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    #Remember if the word was in upper case or Title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    #Seperate the consonants at the start of this word:
    prefixConstants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConstants += word[0]
        word = word[1:]
    
    #Add the Pig Latin ending to the word
    if prefixConstants != '':
        word += prefixConstants + 'ay'
    else:
        word += 'yay'

    #Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    #Add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

    print(' '.join(pigLatin))

