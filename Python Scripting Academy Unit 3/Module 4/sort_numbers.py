
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the numbers in an ascending order
# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`

# The help message should look like:
'''
usage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]

positional arguments:
  numbers     int to be sorted

optional arguments:
  -h, --help  show this help message and exit
  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)
'''

#HINT: use nargs = '*' in an add_argument method
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('number',nargs = '*', type = int, help= "int to be sorted")
parser.add_argument('-s','--save',action="store_true", help= "save the sorted numbers on a file (sorted_numbers.txt)")
args = parser.parse_args()

numbers = []
print(args.number)
for i in args.number:
    numbers.append(i)

numbers.sort()

if args.save:
    file = open('sorted_numbers.txt', 'w')
    for i in numbers:
        file.write(str(i)+"\n")
    print("{} written to sorted_numbers.txt".format(numbers))
else:
    print(numbers)
