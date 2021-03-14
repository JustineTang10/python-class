# Step 1
data = [int(n) for n in open('sensordata.txt').read().split()]
print([i for i in data if -200 <= i <= 200])

"""This was what was in the last homework, so self-explanatory."""

# Step 2
total = 0
for num in data:
  total += num
average = total/len(data)
print(average)
print(sum(data)/len(data))
"""
# Could also be one line.
print(sum(data)/len(data))
"""

# Step 3
counts = [0, 0]
for num in data:
  if num < average:
    counts[0] += 1
  elif num > average:
    counts[1] += 1
print(f"Numbers above average: {counts[1]}\nNumbers below average: {counts[0]}")

"""
# Instead of the whole for loop, counts var could be like this.
counts = [len([a for a in data if a<average]), len([b for b in data if b>average])]
"""
