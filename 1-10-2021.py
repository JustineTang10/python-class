def secret_number():
  import random
  goalnumber = random.randint(1, 50)
  numberoftries = 0
  while True:
    chosennumber = int(input("What number (from 1-50) would you like to choose? "))
    if chosennumber > 50 or chosennumber < 1:
      print("Invalid option, try again")
    elif chosennumber == goalnumber:
      print("That's the number, you win!")
      numberoftries += 1
      break
    elif chosennumber < goalnumber:
      print("That number is too low")
      numberoftries += 1
    else:
      print("That number is too high")
      numberoftries += 1
  tryword = "try" if numberoftries == 1 else "tries"
  print("\nIt took you",numberoftries,tryword,"to guess the number")

 # Version WITH recursion
import random

def secret_number2(goal, tries):
  chosennumber = int(input("What number (from 1-50) would you like to choose? "))
  won = False
  if chosennumber > 50 or chosennumber < 1:
    print("Invalid option, try again")
  elif chosennumber == goal:
    print("That's the number, you win!")
    tries += 1
    won = True
  elif chosennumber < goal:
    print("That number is too low")
    tries += 1
  else:
    print("That number is too high")
    tries += 1
  if won:
    tryword = "try" if tries == 1 else "tries"
    print("\nIt took you",tries,tryword,"to guess the number")
  else:
    secret_number2(goal, tries)

secret_number2(random.randint(1, 50), 0)
