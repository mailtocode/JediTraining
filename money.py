initial_investment_amt = float(input("Enter the initial investment amount: "))

air = float(input("Enter the annual interest rate: "))

noy = int(input("number of years invested: "))

current_money = initial_investment_amt * (1 + air/100) ** noy

print(f"The initial amount $ {initial_investment_amt} "
      f"after {noy} years with interest "
      f"rate {air}% is $ {round(current_money,2)}")
