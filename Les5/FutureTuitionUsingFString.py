tuition = 10000   
year = 0 # Year 0

while tuition < 20000:
    tuition = tuition * 1.07
    year += 1

print("Tuition will be doubled in", year, "years")
print(f"Tuition will be ${tuition:.2f} in {year} years")

