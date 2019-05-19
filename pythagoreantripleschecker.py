'''

MAIN GOAL

Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.

SUBGOALS

If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.

Loop the program so the user can use it more than once without having to restart the program. 

'''

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