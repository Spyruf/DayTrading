cur = float(input("Initial Investment: "))

dailyPercent = float(input("Percent increase per Day: "))
days = int(input("How many days: "))

for x in range(days):
    cur = cur*(1.00 + dailyPercent)
    print(cur)
