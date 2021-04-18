cheese = [3, 2, 5, 6, 7, 3, 2]
crackers = [4, 5, 6, 7, 3, 5, 7]
name = ['Max','Felix','Alex','Vivian','Ethan','Justine','Troy']

# number 1
def histogram(l):
  d = {}
  for item in l:
    d.setdefault(item, 0)
    d[item] += 1

  return d

print(histogram(cheese))

# number 2
def dictmaker(keylist, valuelist): # same thing as last time
  if len(keylist) != len(valuelist):
    return

  d = {}
  for i in range(0, len(keylist)):
    d[keylist[i]] = valuelist[i]    

  listmax = max(list(d.values()))

  return d, list(d.keys())[list(d.values()).index(listmax)]

cheesedict = dictmaker(name, cheese)[0]
crackerdict = dictmaker(name, crackers)[0]
print(cheesedict)
print(crackerdict)

# number 3
def dictlookup(d, target):
  return [key for key in d if d[key] == target]

print(dictlookup(cheesedict, 3))
print(dictlookup(crackerdict, 7))
