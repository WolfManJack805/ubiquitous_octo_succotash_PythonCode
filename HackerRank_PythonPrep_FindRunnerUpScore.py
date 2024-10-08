
if __name__ == '__main__':
    import string
#we are to find the scores runner up
#the first input would be: 10 for the range
#the next input would be the map @arr : 2, 6, 4, 4, 3, 6, 6, 2, 3, 5
#i should prolly see if i could sort the thing and get rid of any duplicates


#here we are taking in the input for the amount of inputs and nums for map

    print("Please enter in the number of scores you would have:", end = "")
    numOfInputs = int(input())
    print("Please enter in each score followed by a space:", end= "")
    scoresMapArr = map(int, input().split())

    print("Here are the current scores entered:", end = "")
    myList = list(scoresMapArr)
    print(myList)

    myCopiedList= myList.copy()

    print("Here is my copied list so i do not alter the original list: ", myCopiedList)

    myCopiedList.sort()
    myList.sort()

    print("Here is my copied list sorted:", myCopiedList)

    i = 0
    j = 1
    
    listLen = len(myCopiedList)
    print("Here is my list lenght:", listLen)
    for i in range(listLen):

        if(j != listLen):
            if(myCopiedList[i] < myCopiedList[j]):
                print( f"I would be greater than j. Comparing:" , myCopiedList[i], "with" , myCopiedList[j])
            elif(myCopiedList[j] > myCopiedList[i]):
                print(f"J would be greater than I. Comparing:", myCopiedList[i], "with" , myCopiedList[j])
            else:
                print(f"J would be equal to I. Comparing:", myCopiedList[i], "with" , myCopiedList[j])
                myList.remove(myCopiedList[i])
        j+= 1

    print(myList)
    print(myList[-2])

    



        
