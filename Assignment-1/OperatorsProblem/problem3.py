# 3. Write a program to convert total days into years, weeks, and remaining days.
total_days = int(input("Total days: "))

years = total_days // 365
remaining = total_days % 365
weeks = remaining // 7
days = remaining % 7

print(f"{total_days} days = {years} years, {weeks} weeks, {days} days")