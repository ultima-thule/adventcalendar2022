name = input("Enter your name: ")
age = input("Enter your age: ")
copies = input("Enter copies no: ")
year100 = 2022 - int(age) + 100
for i in range(0, int(copies)):
    print(f"{name}, you will turn 100 in {year100}")
