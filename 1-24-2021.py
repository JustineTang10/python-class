import random

def comparison(x, y):
  if not x.isnumeric() or not y.isnumeric():
    return None
  elif x < y:
    return -1
  elif x == y:
    return 0
  else:
    return 1

choices = list('0123456789') + ['true', 'false']
choicelist = random.choices(choices, k=2)
print(comparison(choicelist[0], choicelist[1]))
print(choicelist)
