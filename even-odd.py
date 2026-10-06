numbers = (10, 15, 20, 25, 30, 35, 40, 45, 50)
evencount = 0
oddcount = 0
for num in numbers:
  if num % 2 == 0:
    evencount += 1
  else:
    oddcount += 1
print("Even numbers:", evencount)
print("Odd numbers:", oddcount)