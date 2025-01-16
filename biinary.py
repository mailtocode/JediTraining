num = int(input("Enter a number: "))

result = ""

while num > 0:
    remainder = num % 2
    result = str(remainder) + result
    num = num // 2

print(f"The result is {result}")

deci_result = 0
max = len(result) - 1

for achar in result:
    digit = int(achar)
    deci_result = deci_result + digit * (2 ** max)
    max = max - 1

print("Decimal result " + str(deci_result))

