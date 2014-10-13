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



#===============================================================================
#
#   Index of Functions (in order of declaration)
#
#   begin       
#   cls         
#   initRange   
#   promptUser  
#   main        
#
#===============================================================================



#===============================================================================
#
#   begin(data)
#
#   data is a list containing [[start, end], rem, secret]
#
#===============================================================================
def begin(data):
  secret = data[2]
  while True:    
    guess = promptUser(data)
    data[1] -= 1
    guesses = data[1]    
    
    if guess == secret:
      print("You WIN! The secret number is {}".format(secret))
      exit()
    elif guesses == 0:
      print("You LOSE! The secret number is {}".format(secret))
      exit()
    elif secret < guess:
      print("The secret number is less than {}.\n".format(guess))
    else:
      print("The secret number is greater than {}.\n".format(guess))
    

    
#===============================================================================
#
#   cls()
#
#   clear console screen
#
#===============================================================================
def cls():
    os.system(['clear','cls'][os.name == 'nt'])


  
#===============================================================================
#
#   initRange()
#
#   return: list holding a numeric range
#   (ex. [1, 100])
#
#===============================================================================
def initRange():
  range = []  
  start = 1
  
  msg = "Range of numbers will go from 1 through "
  end = int(input(msg))
  if end < 10:
    end = 10
  elif end <= start:
    end = start * 10
    
  cls()
  range.append(start)
  range.append(end)
  return range



#===============================================================================
#
#   promptUser(data)
#
#   prompt user for their guess and validate it
#
#===============================================================================
def promptUser(data):
  # I like passing a list of data around in functions like this, but below
  # looks a bit ugly because it's not immediately obvious what data[0][0]
  # is supposed to be; not sure what to do about that.
  start = data[0][0]
  end = data[0][1]
  rem = data[1]
  
  msg = "Type QUIT to quit.\n\n"
  msg += "I am thinking of a number from {} to {}.\n\n".format(start, end)
  msg += "You have {} guesses remaining.\n".format(rem)
  
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
      
      if guess < start or guess > end:
        print(error)        
      
      else:        
        valid = True
    
    except ValueError:      
      print(error)
    # end while 
  
  cls()
  return guess



#===============================================================================
#
#   main()
#
#===============================================================================
def main():
  cls()
  
  data = []
  
  range = initRange()
  data.append(range)
  
  # starting remaining guesses
  rem = math.floor(math.log(range[1], 2))
  data.append(rem)
  
  secret = random.randint(1, range[1])
  data.append(secret)
  
  begin(data)
  
main()