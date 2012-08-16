setA = [10,22,42,59,61,63,65,83,85,90,93]
setB = [36,53,54,56,69,84,88]

setA = sorted(setA)
setB = sorted(setB)

setAsize = len(setA)
setBsize = len(setB)

setAmarked = []
setBmarked = []

for datapoint in setA:
	setAmarked.append([datapoint,'A'])

for datapoint in setB:
	setBmarked.append([datapoint,'B'])

combinedSet = sorted(setAmarked + setBmarked)

#print combinedSet

setAranks = []
setBranks = []

for rank, data in enumerate(combinedSet):
	if data[1] == 'A':
		setAranks.append(rank + 1)

	elif data[1] == 'B':
		setBranks.append(rank+1)


setArankTotal = sum(setAranks)
setBrankTotal = sum(setBranks)

if setAsize <= setBsize:
	rankSum = setArankTotal
else: 
	rankSum = setBrankTotal



zNumerator = rankSum - (0.5 * setAsize * (setAsize + setBsize + 1))

if zNumerator >= 0:
	zNumerator += 0.5
else:
	zNumerator -= 0.5


zDenominator = ((1.0/12) * setAsize * setBsize * (setAsize + setBsize + 1)) ** 0.5

z = zNumerator / zDenominator

print "A raw data : ", setA
print "B raw data : ", setB

print "Set A ranks : ", setAranks
print "Set B ranks : ", setBranks

print "Set A size : ", setAsize
print "Set B size : ", setBsize

print "Set A rank total : ", setArankTotal
print "Set B rank total : ", setBrankTotal

print "Rank Sum (Rm) : ", rankSum 

print "Z numerator : ", zNumerator
print "Z zDenominator : ", zDenominator 
print "Z : ", z

