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

"""
Got a different data set? Try this function - though it's very picky:
  - it assumes there is a first header row
  - it can only use one column as the 'string keys' it outputs
There might also be other bugs in the program - see if you can fix them!
"""

def average(file):
  try:
    with open(file) as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      data = {'count': {}}
      first = True
      firstrow = []
      l = []
      second = False
      ind = -1
      for row in csvreader:
        if first:
          firstrow = row
          first = False
          second = True
          continue
        elif second:
          for item in row:
            try: float(item)
            except:
              if ind != -1:
                raise ValueError
              else:
                ind = row.index(item)
          for thing in firstrow:
            if firstrow.index(thing) != ind:
              data[thing] = {}
          second = False

        data['count'].setdefault(row[ind], 0)
        data['count'][row[ind]] += 1
        for v in list(data.keys()):
          if v == 'count':
            continue
          data[v].setdefault(row[ind], 0)
          data[v][row[ind]] += float(row[list(data.keys()).index(v)-1])

      averages = {}
      for key in data:
        if key == 'count': continue
        averages[key] = {}
        for datakey in data[key]:
          averages[key][datakey] = data[key][datakey]/data['count'][datakey]

      return averages
  except FileNotFoundError:
    return "The file doesn't exist"
  except ValueError:
    return "The data isn't numbers"
  except IndexError:
    return "Are all your rows the same length?"
