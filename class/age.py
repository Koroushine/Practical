def cal_age(birth_year):
    age = 2025 - birth_year
    return age

print("Age calculator")
birth_year = int(input("Enter your birth year: "))
age = cal_age(birth_year)
print(f"You are {age} years old.")