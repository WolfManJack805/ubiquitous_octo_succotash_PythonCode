if __name__ == '__main__':

    print("Please input the number of commands:", end = "")
    numOfCommands = int(input())
    myList = []
    counter = 0
    keywordInsert = "insert"
    keywordPrint = "print"
    keywordAppend = "append"
    keywordSort = "sort"
    keywordPop = "pop"
    keywordReverse = "reverse"
    keywordRemove = "remove"
    
    while(counter < numOfCommands):
        counter +=1
        print("Here your on interation number", counter)
        keyword = ''
        #the input coming from here has the full string#
        print("Plese put in the full opertation requested:", end = "")
        keyword = input()
        parts = keyword.split()

        print("Here are all parts in the array:",parts)
        print("Here we are checking parts at:", parts[0])
            
        if parts[0] == keywordInsert:
            myList.insert(int(parts[1]),int(parts[2]))
            
        elif parts[0] == keywordReverse:
            myList.reverse()
            
        elif parts[0] == keywordAppend:
            myList.append(int(parts[1]))
            
        elif parts[0] == keywordSort:
            myList.sort()
            
        elif parts[0] == keywordPop:
            myList.pop()
            
        elif parts[0] == keywordRemove:
            myList.remove()
            
        elif parts[0] == keywordPrint:
            print(myList)
        else:
            print("We fell thru all expressions. Better Luck next time! =)")
        
