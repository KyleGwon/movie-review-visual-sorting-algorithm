import re
def customBubbleSort(words, ratings):
	exchanges = True
	passNum = len(ratings)-1
	while passNum > 0 and exchanges:
		exchanges = False
		for i in range(passNum):
			a, b = i, i + 1
			if ratings[a] < ratings[b]:
				exchanges = True
				ratings[a], ratings[b], words[a], words[b] = ratings[b], ratings[a], words[b], words[a]
		passNum -= 1
	return words, ratings
def getWords(text):
	return re.compile("\w+").findall(text)
def getStopWords():
	file = open("words.txt", "r")
	wordsToIgnore = []
	for word in file.readlines():
		tempWord = []
		for letter in word:
			if letter.isalpha() and word.index(letter) != len(word)-1:
				tempWord.append(letter)
		realWord = "".join(tempWord)
		wordsToIgnore.append(realWord)
	return wordsToIgnore
def getReviews(file):
	reviews = []
	loopFile = open(file, "r")
	file = open(file, "r")
	for i in range(len(loopFile.readlines())):
		review = file.readline()
		reviews.append(review)
	return reviews
def getInfo(file):
	ratings = []
	words = []
	reviews = getReviews(file)
	reviewWords = []
	for review in reviews:
		reviewWords.append(getWords(review))
	for review in reviewWords:
		for i in range(len(review)):
			if review[i].isnumeric():
				pass
			elif review[i].lower() not in getStopWords() and review[i].isalpha() and review[i].lower() not in words:
				words.append(review[i])
				ratings.append([int(review[0])-2])
			else:
				if review[i].lower() not in getStopWords() and review[i].isalpha():
					temp = []
					for index in range(len(ratings[words.index(review[i])])):
						temp.append(ratings[words.index(review[i])][index])
					temp.append(int(review[0])-2)
					ratings[words.index(review[i])] = temp\
	return words, ratings
def transformInfo(file):
	data = getInfo(file)
	ratings = data[1]
	tempRatings = []
	for i in range(len(ratings)):
		temp = int(sum(ratings[i]) / len(ratings[i]))
		tempRatings.append(temp)
	newRatings = customBubbleSort(data[0], tempRatings)[1]
	newWords = customBubbleSort(data[0], tempRatings)[0]
	return newWords, newRatings
def main():
	file = "smallReviews.txt"
	words = transformInfo(file)[0]
	ratings = transformInfo(file)[1]
	for i in range(len(words)):
		print(ratings[i], words[i])
main()
