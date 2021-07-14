# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


# def dicetoorderedhand(a, b, c):
# 	# your code goes here
# 	l = [a,b,c]
# 	l.sort(reverse=True)
# 	string = []
# 	strings = [str(i) for i in l]
# 	# string = "".join(strings)
# 	string.append(strings)
# 	return int(string)
# print(dicetoorderedhand(6,5,6))

def dicetoorderedhand(a, b, c):
	# your code goes here
  l = [a,b,c]
  l.sort(reverse=True)
  string = []
  strings = [str(i) for i in l]
  # print(strings)
	# string = "".join(strings)
  # string.append(strings)
  # print(string)
  # val = string.split()
  str_val = ""
  for i in strings:
    str_val += i
  # print(int(str_val))

  return int(str_val)
# print(dicetoorderedhand(6,5,6))


# strings = 656