# data from last time(s)
cheese = [3, 2, 5, 6, 7, 3, 2]
crackerdict = {'Max': 4, 'Felix': 5, 'Alex': 6, 'Vivian': 7, 'Ethan': 3, 'Justine': 5, 'Troy': 7}

# histogram (made last week)
def histogram(l):
  d = {}
  for item in l:
    d.setdefault(item, 0)
    d[item] += 1

  return d

print(histogram(cheese))

# invert
def invertdict(d):
  invertd = {}
  for key in d:
    invertd.setdefault(d[key], [])
    invertd[d[key]].append(key)

  return invertd

print(invertdict(crackerdict))
