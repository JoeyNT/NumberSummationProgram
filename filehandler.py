# Change your program from 27.2 so that it reads a file called numbers.txt in which each line might also contain more or fewer than three numbers. Each line will also follow this rule: the first number in the line indicates the number of numbers after it.

# Here is an example of what numbers.txt might look like:

# 3 10 20 23
# 4 -7 8 15 12
# 0
# 1 17
# 5 -8 113 -1 6 2
# Your program should compute the sum of all numbers except the first number in each row. Your results should then be written to a file called output.txt. Each sum should be on its own line.

# If numbers.txt held the information above, output.txt should hold the following after your program runs:

# 63
# 28
# 0
# 17
# 112

import pickle

numbersfile= open ('numbers.txt','r')# as pickle_file:
sumfile = open('output.txt','w')
for line in numbersfile:
  numberSum = 0
  number = line.split()
  print(number)
  for n in number:
    print(n)
    numberSum += int(n)
  print(numberSum)
  sumfile.write(str(numberSum) + "\n")

numbersfile.close()
sumfile.close()
