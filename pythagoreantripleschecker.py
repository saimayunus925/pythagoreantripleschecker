def is_Pythagorean_Triple(a, b, c):
  sum = a**2 + b**2
  if sum == c**2:
    return True
  else:
    return False

print("PYTHAGOREAN TRIPLES CALCULATOR\n")

num = int(input("# OF TIMES TO DO CALCULATION: "))
i = 0

while i < num:
  a1 = float(input("\nEnter a: \n"))
  b1 = float(input("Enter b: \n"))
  c1 = float(input("Enter c: \n"))

  pythagoras = is_Pythagorean_Triple(a1, b1, c1)

  if(pythagoras):
    print("\nThese values are a Pythagorean Triple.\n")
  else:
    print("These values aren't a Pythagorean Triple.")
  
  i += 1
