salary_per_month = 25000
target = 50000
increase_rate = 0.03
years = 0

while salary_per_month < target:
    salary_per_month *= (1 + increase_rate)
    years += 1
print(f"It'll take {years} years for the salary to double, reaching {salary_per_month:.2f} dollars per month.")