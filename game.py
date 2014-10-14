#   A Game of Numbers (and Guessing)
#
#   Easy mode:
#     For the range end value, enter a value that equals a power of 2 (ex. 128)
#
#     This will give the player enough guesses to always win by using
#     a binary search pattern.
#
#   Hard mode:
#     For the range end value, enter a value that equals a (power of 2) -1 (ex. 127)
#
#     With one remaining guess, using a binary search pattern, there
#     will remain several valid numbers to choose from.



import math
import random
import os

data = {'start':1, 'end':10, 'remaining_guesses': 0, 'secret':0}
   

def cls():
    os.system(['clear','cls'][os.name == 'nt'])


def promptUser():  
  msg = "Type QUIT to quit.\n\n"
  msg += "I am thinking of a number from {} to {}.\n\n".format(data['start'], data['end'])
  msg += "You have {} guesses remaining.\n".format(data['remaining_guesses'])
  
  valid = False  
  while not valid:    
    guess = input("{}> ".format(msg))
    error = "\n{} is not a valid guess!".format(guess)
    
    if guess == "QUIT":
      exit()    
      
    cls()    
    try:      
      # if casting to an int fails, an exception will be thrown      
      guess = int(guess)
      
      if guess < data['start'] or guess > data['end']:
        print(error)        
      
      else:        
        valid = True
    
    except ValueError:      
      print(error)
    # end while 
  
  cls()
  return guess


def main():
  cls()
  
  msg = "Range of numbers will go from 1 through "
  data['end'] = int(input(msg))
  if data['end'] < 10:
    data['end'] = 10
  elif data['end'] <= data['start']:
    data['end'] = data['start'] * 10
    
  cls()
  
  # starting remaining guesses
  data['remaining_guesses'] = math.floor(math.log(data['end'], 2))
  
  data['secret'] = random.randint(1, data['end'])
  
  while True:    
    guess = promptUser()
    data['remaining_guesses'] -= 1   
    
    if guess == data['secret']:
      print("You WIN! The secret number is {}".format(data['secret']))
      exit()
    elif data['remaining_guesses'] == 0:
      print("You LOSE! The secret number is {}".format(data['secret']))
      exit()
    elif data['secret'] < guess:
      print("The secret number is less than {}.\n".format(guess))
    else:
      print("The secret number is greater than {}.\n".format(guess))
  
main()
