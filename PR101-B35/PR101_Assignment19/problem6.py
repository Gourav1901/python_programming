# Find the Average
# Write a function named calculateAverage that takes an array of numbers as input and returns the average (mean) of those numbers.
# Sample Input: [10, 15, 20, 25]
# Sample Output: 17.5
def calculateAverage(numbers):
  if not numbers:
    return 0  
  else:
    return sum(numbers) / len(numbers)


input_numbers = [10, 15, 20, 25]
output = calculateAverage(input_numbers)
print("Output:", output) 