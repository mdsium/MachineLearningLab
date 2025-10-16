# 5. Write a program to compute simple interest and compound interest.
P = float(input("Principal: "))
R = float(input("rate: "))
T = float(input("Time in year: "))


simple_interest = (P * R * T) / 100
compound_interest =  P *((1+R/100)**T)-P

print("Simple interest: ", simple_interest)
print("compound interest: ", compound_interest)