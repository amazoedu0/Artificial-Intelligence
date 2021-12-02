import os


def menu():
    # print("1 - Meter to Kilometer\n2 - Kilometer to Meter\n3 - Centimeter to Meter\n4 - Centimeter to Milimeter\nCHOICE:")
    choice = int(input(
        "1 - Meter to Kilometer\n2 - Kilometer to Meter\n3 - Centimeter to Meter\n4 - Centimeter to Milimeter\n99 - QUIT\n\nCHOICE : "))
    return choice


def meterToKilometer(data):
    return data/1000

# kilometer to meter


def kilometerToMeter(data):
    return data*1000

# cewntimeter to meter


def centimeterToMeter(data):
    return data/100

# centimeter to milimeter


def centimeterToMillimeter(data):
    return data*10
# MAIN


choice = 0
while 1:
    os.system('cls')
    choice = menu()
    if choice == 99:
        print("\nAllah Hafiz!")
        break
    data = int(input("\nValue : "))
    if choice == 1:
        print(f"\nKilometer: {meterToKilometer(data)}")
    elif choice == 2:
        print(f"\nMeter: {kilometerToMeter(data)}")
    elif choice == 3:
        print(f"\nMeter: {centimeterToMeter(data)}\n")
    elif choice == 4:
        print(f"\nMillimeter: {centimeterToMillimeter(data)}\n")
    else:
        print('\nINVALID CHOICE!')
    os.system('pause')


print('\n\nWhile Ends Here!')
