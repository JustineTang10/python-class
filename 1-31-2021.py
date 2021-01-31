def is_between(x, y, z):
  if x <= y <= z:
    return True
  else:
    return False

import random
numbers = list("0123456789")
chosenlist = [int(random.choice(numbers)) for i in range(3)]
print(is_between(chosenlist[0], chosenlist[1], chosenlist[2]))
print(chosenlist)
