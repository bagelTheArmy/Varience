dict = { }

FinalTable = []

# open dictionary file and put it into dictionary
f = open('dictionary.txt', 'r')
for line in f:
    splitLine = line.split()
    dict[splitLine[0]] = splitLine[1]
    dict[splitLine[1]] = splitLine[0]
f.close()

#check for varience add all combos to FinalTable
FinalTable = []
f = open('table.txt', 'r')
for line in f:
    splitLine = line.split()

    varianceCombos = []
    varienceStrings = []
    for x in range(0,len(splitLine)):
        if splitLine[x] in dict:
            varianceCombos.append(x)
    varienceStrings.append(line.rstrip("\n"))
    for x in varianceCombos:
        orignalLength = len(varienceStrings)
        for y in range(0,orignalLength):
            splitThis = varienceStrings[y].split()
            splitThis[x] = dict[splitThis[x]]
            string = ""
            for z in range(0,len(splitThis)):
                if z!=0:
                    string = string+" "+splitThis[z]
                else:
                    string = string + splitThis[z]
            varienceStrings.append(string)
    for x in varienceStrings:
        FinalTable.append(x)
print(FinalTable)
f.close()
file = open("finalTable.txt","w")
for x in FinalTable:
    file.write(x+"\n")

file.close()




#except:
    #print("something went wrong")