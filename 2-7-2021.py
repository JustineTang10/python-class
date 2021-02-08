def oops():
  loop = 0
  while loop < 3:
    loop += 1
    print('oops')

def passwordcheck():
  password = 'dog'
  userguess = input("Please input a password to grant access. ")
  tries = 1
  while userguess != password:
    print("That is the wrong password. Try again.")
    userguess = input("Please input a password to grant access. ")
    tries += 1
  
  return [tries, 'try' if tries == 1 else 'tries']

data = passwordcheck()
print(f'It took you {data[0]} {data[1]}')
