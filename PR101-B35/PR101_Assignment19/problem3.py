# Calculate Area and Perimeter
# Write two functions to calculate the area and perimeter of a rectangle.
# Use the functions to calculate the area and perimeter of given dimensions
def calculate_area(length, width):
  return length * width

def calculate_perimeter(length, width):
  return 2 * (length + width)

# Test the functions
length = 6
width = 5

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"The area of the rectangle with length {length} and width {width} is: {area}")
print(f"The perimeter of the rectangle with length {length} and width {width} is: {perimeter}")