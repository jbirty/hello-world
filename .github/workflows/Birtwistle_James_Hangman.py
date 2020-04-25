from random import choice #Import choice function from random package

with open('word_list.txt') as f: #Use a “with” loop to open text file
  word_list = [line.strip('\n') for line in f] # turn text file into a list of strings, deleting the newline characters
  original_word = choice(word_list) #Choose a random word from the text file

def word_check(original_word, word_so_far, guess): #Define check and de-star function
  if guess not in original_word:
    return(False, word_so_far) #If the guess is not in the word, return “False” for whether the guess was correct, and word_so_far unchanged
  else:
    word_now = '' #Empty string to build new word from
    for i in range(len(original_word)): #Loop through each letter at a time
      if original_word[i] == guess:
        word_now += guess #If the guess matches this letter of the original word, insert guess letter here
      else:
        word_now += word_so_far[i] #Otherwise, insert whatever letter was already at this point in word_so_far
    return(True, word_now) #Return "True" for whether the guess was correct, and word_now with the correct guess added
  
word_so_far = '*' * len(original_word) #Create word so far – just stars at this stage

guess = ''
wrong_guesses = 0
while wrong_guesses < 7: #Start a loop while wrong_guesses < 7

  print('You have made {} wrong guesses so far.\nThe word so far is: {}'.format(wrong_guesses, word_so_far))
  guess = input('Please enter your next guess: ').lower
   #Take guess, drop to lower case, ignore all but the first character; non-letter characters could be entered, but will simply register as a wrong guess

  correct_guess, word_so_far = word_check(original_word, word_so_far, guess) #Check and de-star
  if correct_guess:
    print('Good guess, {} is in the word'.format(guess))
  else:
    print('Wrong, {} is not in the word'.format(guess))
    wrong_guesses += 1
  if word_so_far == original_word:
    break #If all stars have been cleared, break out of the while loop

if wrong_guesses == 7:
  print('you lose') #If the while loop finished because of 7 wrong guesses, print loss statement

else:
  print('congratulations you win') #If the while loop finished because all letters were correctly guessed, print win statement
