# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
# 	n = len(a)
# 	# if (n == 0) and (n == 1):
# 	# 	return True
# 	value1 = 0
# 	value2 = 0
# 	for i in range(n):
# 		value1 += a[i][i]
# 		value2 += a[i][n-i-1]

# 	# print(value1)
# 	print(value2)
# ismostlymagicsquare([ [ 1,2,3,4],[ 2,1,4,5]])	
	n = len(a)
	if (n==1):
		return True


	value1 = 0
	value2 = 0
	for i in range(n):
		value1 += a[i][i]
		value2 += a[i][n-i-1]
	# print(value1)
	# print(value2)	
	sum_value1 = 0
	sum_value2 = 0
	for i in range(n):
		for j in range(n):
			sum_value1 += a[i][j]
			# print(sum_value1)
			sum_value2 += a[j][i]
		return value1 == value2 ==sum_value1 == sum_value2
	# print(sum_value1)		
	
# a = ismostlymagicsquare([[1,2,3],[2,1,4],[3,2,1]])
# print(a)

# 1 2 3
# 2 1 4
# 3 2 1

# 1+1+1
# 3+

# [0,0]  = 1
# [1,0][1,1] 2+1
# [2,0][2,1][2,2] 3+2+1 