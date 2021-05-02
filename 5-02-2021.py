# once again, the data
cheese = [3, 2, 5, 6, 7, 3, 2]
crackers = [4, 5, 6, 7, 3, 5, 7]
name = ['Max','Felix','Alex','Vivian','Ethan','Justine','Troy']

# number 1
cheesenames = zip(name, cheese)
morethanfive = [p[0] for p in cheesenames if p[1] > 5]
print(morethanfive)

# number 2
data = zip(name, cheese, crackers)
dictionary = {d[0]: d[1]+d[2] for d in data}
highest = max(dictionary, key=lambda x: dictionary[x])
print(highest)
