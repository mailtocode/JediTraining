# age is a variable. '=' is an operator and 10 is a literal
can_afford = float(input("How much can you pay: "))
loan_amount = float(input("Enter your loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
no_of_years = int(input("Enter number of years: "))

actual_interest = annual_interest_rate / 100
monthly_interest_rate = actual_interest / 12
no_of_months = no_of_years * 12
comp1 = (1 + monthly_interest_rate) ** no_of_months
monthly_payment = (loan_amount * monthly_interest_rate * comp1) / (comp1 - 1)
print("Monthly Payment: ", round(monthly_payment, 2))

total_amount = monthly_payment * no_of_months

print("Total Amount2: ", round(total_amount, 2))

if monthly_payment <= can_afford:
    print("Approved")
    print("Month No| Monthly Payment | Principal Paid | Interest Paid | Remaining Loan Amount")
    amount_remaining = loan_amount
    month_no = 1
    while amount_remaining > 0:
        interest_paid = amount_remaining * monthly_interest_rate
        principal_paid = monthly_payment - interest_paid
        amount_remaining = amount_remaining - principal_paid
        print(f"{month_no}| {round(monthly_payment,2)} | {round(principal_paid,2)} | {round(interest_paid, 2)} "
              f"| {round(amount_remaining,2)}")
        month_no = month_no + 1
else:
    print("Rejected")
print("Thanks")
