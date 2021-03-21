letters = open('letters.txt').read().splitlines()
lcount = {l:letters.count(l) for l in letters}
print(f'Letter A showed up {lcount["A"]} times.')
