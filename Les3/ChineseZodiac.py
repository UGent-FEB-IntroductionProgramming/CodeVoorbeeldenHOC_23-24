year = int(input("Geef je geboortejaar:"))

zodiac_number = year % 12
chinese_zodiac = ""

if zodiac_number == 0:
    chinese_zodiac = "monkey"
elif zodiac_number == 1:
    chinese_zodiac = "rooster"
elif zodiac_number == 2:
    chinese_zodiac = "dog"
elif zodiac_number == 3:
    chinese_zodiac = "pig"
elif zodiac_number == 4:
    chinese_zodiac = "rat"
elif zodiac_number == 5:
    chinese_zodiac = "ox"
elif zodiac_number == 6:
    chinese_zodiac = "tiger"
elif zodiac_number == 7:
    chinese_zodiac = "rabbit"
elif zodiac_number == 8:
    chinese_zodiac = "dragon"
elif zodiac_number == 9:
    chinese_zodiac = "snake"
elif zodiac_number == 10:
    chinese_zodiac = "horse"
else:
    chinese_zodiac = "sheep"

print("Your Chinese zodiac is", chinese_zodiac)