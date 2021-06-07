import csv, random

# GETTING THE DATA
with open('iris.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  c = {} # count

  sl = {} # sepal length
  sw = {} # sepal width
  pl = {} # petal length
  pw = {} # petal width
  s_ratio = {} # sepal ratios
  p_ratio = {} # petal ratios

  for row in csvreader:
    try: temp = float(row[0])
    except: continue

    c.setdefault(row[4], 0)
    c[row[4]] += 1

    # getting all the values, per measurement
    for v in [sl, sw, pl, pw]:
      v.setdefault(row[4], [])
    sl[row[4]].append(float(row[0]))
    sw[row[4]].append(float(row[1]))
    pl[row[4]].append(float(row[2]))
    pw[row[4]].append(float(row[3]))

    # getting the ratios' total (and later average)
    for w in [s_ratio, p_ratio]:
      w.setdefault(row[4], 0)
    s_ratio[row[4]] += float(row[0])/float(row[1])
    p_ratio[row[4]] += float(row[2])/float(row[3])

# INPUTTING AND GENERATING
while True:
  species = input('Input a species to generate random sepal and petal measurements (choices: setosa, versicolor, virginica) ')
  if species.lower() in ['setosa', 'versicolor', 'virginica']:
    break
  print('Invalid option, try again')
species = species.lower()

random_sl = round(random.random() * (max(sl[species]) - min(sl[species])) + min(sl[species]), 1)
random_sw = round(random.random() * (max(sw[species]) - min(sw[species])) + min(sw[species]), 1)
random_pl = round(random.random() * (max(pl[species]) - min(pl[species])) + min(pl[species]), 1)
random_pw = round(random.random() * (max(pw[species]) - min(pw[species])) + min(pw[species]), 1)


''' # DELETE TRIPLE QUOTES (AND ADD AS NEEDED) TO TEST OUT

# print out all random-generated values
print(f"""Sepal length: {random_sl} cm
Sepal width: {random_sw} cm
Petal length: {random_pl} cm
Petal width: {random_pw} cm
""".rstrip())

# print out values based on ratios
print(f"""Sepal length: {random_sl} cm
Sepal width: {round(random_sl/(s_ratio[species]/c[species]), 1)} cm
Petal length: {random_pl} cm
Petal width: {round(random_pl/(s_ratio[species]/c[species]), 1)} cm
""".rstrip())
'''

with open('iris.csv', 'a') as csv_file:
  csvwriter = csv.writer(csv_file)
  csvwriter.writerow([random_sl, random_sw, random_pl, random_pw, species]) # or the ratio format, whichever you want
