import random 

# Generate random numbers
number1 = random.randint(0,10)
number2 = random.randint(0,10)

# Prompt the user to enter an answer
answer = int(input("What is " + str(number1) + " + " 
    + str(number2) + "? "))
    
# Display result
#if answer == number1 + number2:
 #   print("juist")
#else:
 #   print("fout")

print(answer == number1 + number2)

