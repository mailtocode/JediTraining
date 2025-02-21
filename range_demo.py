
previous = 0
aval = 1
anotherval = 0
for something in range(5,20):
    print(f"Current Number {something} Previous Number  {previous}  Sum:  {something + previous}")
    previous = something * 5
