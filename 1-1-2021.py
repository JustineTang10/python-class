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
