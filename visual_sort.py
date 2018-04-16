import random
import time
def generateRandomList(lenOfList, rangeOfNum):
	lst = []
	for i in range(len("ffffff")):
		num = random.randint(rangeOfNum[0], rangeOfNum[1])
		lst.append(num)
	return lst
def sortList(lst):
	print("Original list: %s" % (lst))
	for item in lst:
		print("%s -- %d" % ("*"*item, item))
	continueInput = input("\nPress 'Enter' to continue: \n")
	for i in range(len(lst)):
		item = lst[i]
		minimum = min(lst[i:])
		minimumIndex = lst.index(minimum)
		a, b = i, minimumIndex	
		if lst[a] == lst[b]:
			change = False
		else:
			change = True
		print("The minimum value in %s is %d" % (lst[i:], minimum))
		if change:
			print("Swap %d and %d" % (lst[a], lst[b]))
		else:
			print("No change")
		lst[a], lst[b] = lst[b], lst[a]
		for item in lst:
			print("%s -- %d" % ("*"*item, item))
		continueInput = input("\nPress 'Enter' to continue: \n")
	print("Sort complete\n")
	time.sleep(1)
	print("Final list: %s" % (lst))
	for item in lst:
		print("%s -- %d" % ("*"*item, item))
def main():
	lenOfList = 6
	minimum = 0
	maximum = 20
	rangeOfNum = [minimum, maximum]
	lst = generateRandomList(lenOfList, rangeOfNum)
	sortList(lst)
main()
