tuition = 2000
year = 0 # Year 0
percentage = 0.07

while tuition < tuition * 2:
    tuition = tuition * (1 + percentage)
    year += 1

print("Tuition will be doubled in", year, "years")
print("Tuition will be $" + format(tuition, ".2f"), 
      "in", year, "years")

