# Enter your code here. Read input from STDIN. Print output to STDOUT
userStr = list()
t = int(input())
for i in range(t):
    userStr.append(input())

for i in range(t):
    outputStr = ''
    pString = userStr[i]
    counter = 0 #do evens
    while counter < len(pString):
            outputStr = outputStr + pString[counter]
            counter = counter + 2
    outputStr = outputStr + ' '
    counter = 1 #do odds
    while counter < len(pString):
            outputStr = outputStr + pString[counter]
            counter = counter + 2
    print(outputStr)
    