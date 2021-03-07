'''I know we didn't do list comprehensions but why not.'''
numbers = [int(n) for n in open('yelp_review.txt').read().split()]
print([i for i in numbers if 1 < i < 5])

"""
# This could also be:
numbers = open('yelp_review.txt').read().split()
for n in range(len(numbers)):
  numbers[n] = int(numbers[n])

numbers2 = []
for i in numbers:
  if 1 < i < 5:
    numbers2.append(i)

print(numbers2)

# Obviously, it's just easier to use two list comprehensions.
"""
