cp = int(input("Enter the Cost-Price : "))
pp = int(input("Enter the percentage of Profit : "))

total = cp+ (cp* (pp/100))
profit = cp*(pp/100)

print(f'The profit you have earned is : {profit}\nThe Selling price is : {total}')