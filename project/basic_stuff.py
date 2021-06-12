import csv

l = 0 # I guess this stands for "loop", but in reality it's really a tally count

with open('iris.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  for row in csvreader:
    if l == 0:
      print(f'Columns are {", ".join(row)}')
    l += 1
  
  print(f'There are {l} lines.') # counts the 1st line (the header), so there's really 150 lines, not 151

  """Got a different CSV file? Try this function out: """
  def basic_stuff(file):
    try:
      with open(file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
          if l == 0:
            columns = row
          l += 1

        return (columns, l)
    except FileNotFoundError:
      return "File doesn't exist"
