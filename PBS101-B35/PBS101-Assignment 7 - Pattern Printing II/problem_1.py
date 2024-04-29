
print( " "+"*" * 3 + " " * 3 + "*" * 3)
print("*" * 5 + " " + "*" * 5)
for i in range(6, 0, -1):
        # Print spaces before the asterisks
        for j in range(6 - i):
            print(" ", end="")
        # Print asterisks
        for j in range(2 * i - 1):
            print("*", end="")
        print()
  
  
  
