def dictmaker(keylist, valuelist):
  if len(keylist) != len(valuelist):
    return

  d = {}
  for i in range(0, len(keylist)):
    d[keylist[i]] = valuelist[i]    

  listmax = max(list(d.values()))

  return d, list(d.keys())[list(d.values()).index(listmax)]

cheese = [3,2,5,6,7,3,2]
name = ['Max','Felix','Alex','Vivian','Ethan','Justine','Troy']

d = dictmaker(name, cheese)
print(f"{d[1]} brought the most cheese")
print(f"The data: {d[0]}")
