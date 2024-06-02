

# You are given the names and marks of N different students in a hackerrank contest. Your task is to write a program that generates a leaderboard for the students under the following conditions:

# If two students get the same marks, they receive the same rank.      jay   nvn 70   
# The student placed next to students with the same marks will receive a rank that skips the intermediate ranks.   jay nvn nandu grv   70 70 60 50     
# Refer to the sample test case for better understanding.

# Note: You cannot use built-in sort functions. Using them can lead to disqualification. Write your own sorting algorithm.

# Input
# Input Format
# The first line of input contains N.
# The next N lines each contain a name and marks respectively of N different students (where name and marks are separated by a space).
# Constraints
# N < 100
# Output
# Print N names with their rank. Follow these rules for generating the list:

# The students having more marks get a better rank.
# If students have similar marks, their rank will be the same. (In the case of similar marks, the person whose name comes first in alphabetical order comes first in order. However, their rank will be the same.)
# The student placed next to students with the same marks will receive a rank that skips the intermediate ranks.
# Sample Input 1
# 6
# rancho 45                    45 
# chatur 32                      45    
# raju 30                           32
# farhan 28                           30
# virus 32                              28
# joy 45
# Sample Output 1
# 1 joy
# 1 rancho
# 3 chatur
# 3 virus
# 5 raju
# 6 farhan

n = int(input())

students = []

name,marks = input().split()
for _ in range(n):
  students.append(name,int(marks))


for i in range(n):
  for j in range(n-1-i):
    if (students[j][1] < students[j+1][1] 
      or students[j][1] == students[j+1][1]
      and students[j[0]] > students[j+1][0] 
       ):
      students[j],students[j+1] = students[j+1],students[j]

rank = 1
prev_marks = students[0][1]
for i in range(n):
  if students[i][1] != prev_marks:
       rank = i + 1
       prev_marks = students[i][1]
  print(rank,student[i][1])