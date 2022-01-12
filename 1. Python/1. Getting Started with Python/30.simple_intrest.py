"""
Write a Python program to calculate the amount payable if money has been lent on simple interest.
Principal or money lent = P, Rate of interest = R% per annum and Time = T years. Then Simple Interest
(SI) = (P x R x T)/ 100.
Amount payable = Principal + SI.
"""

principal = int(input("Enter the Principal amount: "))
rate = int(input("Enter the rate of the Simple Interest: "))
time = int(input("Enter the time in years: "))

si = (principal*rate*time)/100
payable_amount = principal + si
print("Amount Payable :",payable_amount)