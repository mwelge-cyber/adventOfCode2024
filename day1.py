import fileReader

lines = fileReader.readFile("day1.txt")
# Part 1
leftList=[]
rightList=[]
for line in lines:
    splitline = line.split()
    leftList.append(splitline[0])
    rightList.append(splitline[1])

leftList.sort()
rightList.sort()
totalDistance = 0
for  i, item in enumerate(leftList):
    totalDistance+=abs(int(leftList[i]) - int(rightList[i]))

print(totalDistance)

# Part 2
sim = 0
for item in leftList:
    sim += rightList.count(item)*int(item)

print(sim)