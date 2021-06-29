import csv
import statistics

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  height_weight_data = list(reader)
  
height_weight_data.pop(0)
allheights = []
for h in height_weight_data:
    allheights.append(float (h[1]))

no_of_heights = len(allheights)
sum_of_heights = 0
for n in allheights:
    sum_of_heights = sum_of_heights+n
mean = sum_of_heights/no_of_heights
print (mean)

v = statistics.stdev(allheights)
print (v)