import csv

with open('iris.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  
  # all of these dictionaries have the species as keys
  sl = {} # sepal length
  sw = {} # sepal width
  pl = {} # petal length
  pw = {} # petal width
  c = {} # count
  for row in csvreader:
    try: temp = float(row[0]) # is it a string that can be converted to a number?
    except: continue # no, we've returned an error, next row please

    c.setdefault(row[4], 0) # if key exists, do nothing. if not, make it
    c[row[4]] += 1
    for v in [sl, sw, pl, pw]:
      v.setdefault(row[4], 0)
    sl[row[4]] += float(row[0])
    sw[row[4]] += float(row[1])
    pl[row[4]] += float(row[2])
    pw[row[4]] += float(row[3])

""" # many digits after the decimal version, delete triple quotes to test out
print('- SETOSA -')
print(f'Sepal length: {sl["setosa"]/c["setosa"]}')
print(f'Sepal width: {sw["setosa"]/c["setosa"]}')
print(f'Petal length: {pl["setosa"]/c["setosa"]}')
print(f'Petal width: {pw["setosa"]/c["setosa"]}')

print('- VERSICOLOR -')
print(f'Sepal length: {sl["versicolor"]/c["versicolor"]}')
print(f'Sepal width: {sw["versicolor"]/c["versicolor"]}')
print(f'Petal length: {pl["versicolor"]/c["versicolor"]}')
print(f'Petal width: {pw["versicolor"]/c["versicolor"]}')

print('- VIRGINICA -')
print(f'Sepal length: {sl["virginica"]/c["virginica"]}')
print(f'Sepal width: {sw["virginica"]/c["virginica"]}')
print(f'Petal length: {pl["virginica"]/c["virginica"]}')
print(f'Petal width: {pw["virginica"]/c["virginica"]}')
"""

# rounded version, 1 digit after the decimal
print('- SETOSA -')
print(f'Sepal length: {round(sl["setosa"]/c["setosa"], 1)}')
print(f'Sepal width: {round(sw["setosa"]/c["setosa"], 1)}')
print(f'Petal length: {round(pl["setosa"]/c["setosa"], 1)}')
print(f'Petal width: {round(pw["setosa"]/c["setosa"], 1)}')

print('- VERSICOLOR -')
print(f'Sepal length: {round(sl["versicolor"]/c["versicolor"], 1)}')
print(f'Sepal width: {round(sw["versicolor"]/c["versicolor"], 1)}')
print(f'Petal length: {round(pl["versicolor"]/c["versicolor"], 1)}')
print(f'Petal width: {round(pw["versicolor"]/c["versicolor"], 1)}')

print('- VIRGINICA -')
print(f'Sepal length: {round(sl["virginica"]/c["virginica"], 1)}')
print(f'Sepal width: {round(sw["virginica"]/c["virginica"], 1)}')
print(f'Petal length: {round(pl["virginica"]/c["virginica"], 1)}')
print(f'Petal width: {round(pw["virginica"]/c["virginica"], 1)}')
