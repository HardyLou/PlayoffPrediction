### This file creates appends all the training data from
### the specified range of years into a single training set

fout=open("training.csv","w")

header = 0
# Range is not inclusive of the latter year
for year in range(1990,2011):
  f = open("trainingData/trainingdata_"+str(year)+".csv")

  if header == 0:
    header = 1
  else:
    f.next()  # skip the header

  for line in f:
    fout.write(line)
  f.close()
fout.close()