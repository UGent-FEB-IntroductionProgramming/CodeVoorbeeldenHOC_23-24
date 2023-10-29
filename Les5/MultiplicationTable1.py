print("Multiplication Table")
for x in range(1,10):
    print(x, end = ' ')
print()
print("-----------------------------")

for i in range(1,10):
    print(str(i) + " | ", end = "")
    for j in range(1, 10):
        print(i * j, end=' ')
    print()
