year = int(input("Geef je geboortejaar:"))

zodiac_number = year % 12
chinese_zodiac = ""

match zodiac_number:
    case 0: chinese_zodiac = "monkey"
    case 1: chinese_zodiac = "rooster"
    case 2: chinese_zodiac = "dog"
    case 3: chinese_zodiac = "pig"


print("Your Chinese zodiac is", chinese_zodiac)