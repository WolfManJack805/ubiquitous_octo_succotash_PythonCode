if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    myList = [x,y,z]
    myCopiedList = myList.copy()
    myCopiedList1 = myList.copy()
    print("Here is my current list: ",myList)
    
    #how to create all list orders?!?!?
    i = 0
    j = 1
    lenList= len(myList)
    
    myFinalList = []
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[i])
            myFinalList.append(myList[i])
            myFinalList.append(myList[i])
        
        if(j == 1):
            myFinalList.append(myList[i])
            myFinalList.append(myCopiedList[i])
            myFinalList.append(myCopiedList1[j])
        if(j == 2):
            myFinalList.append(myList[i - 1])
            myFinalList.append(myCopiedList[i - 1])
            myFinalList.append(myCopiedList1[j])
        j += 1
    
    print("Here is my final list:",myFinalList)
    
    i = 0
    j = 1
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[i])
            myFinalList.append(myList[j])
            myFinalList.append(myList[i])
        
        if(j == 1):
            myFinalList.append(myList[i])
            myFinalList.append(myCopiedList[j+ 1])
            myFinalList.append(myCopiedList1[i])
        j += 1
    
    i = 0
    j = 1
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[j])
            myFinalList.append(myList[i])
            myFinalList.append(myList[i])
        if(j == 1):
            myFinalList.append(myList[j + 1])
            myFinalList.append(myCopiedList[i])
            myFinalList.append(myCopiedList1[i])
        j += 1
        
    print("Here is my final list:",myFinalList)
    
    i= 0
    j= 1
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[i + 1])
            myFinalList.append(myList[i + 1])
            myFinalList.append(myList[i + 1])
        if(j == 1):
            myFinalList.append(myList[j + 1])
            myFinalList.append(myCopiedList[j+1])
            myFinalList.append(myCopiedList1[j + 1])
        j += 1
        
    print("Here is my final list:",myFinalList)
    
    i = 0
    j = 1
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[i])
            myFinalList.append(myList[j])
            myFinalList.append(myList[j])
        if(j == 1):
            myFinalList.append(myList[i])
            myFinalList.append(myCopiedList[j + 1])
            myFinalList.append(myCopiedList1[j + 1])
        j += 1
        
    print("Here is my final list:",myFinalList)
    
    i = 0
    j = 1
    for i in range(lenList):
        if(i == 0):
            myFinalList.append(myList[i + 2])
            myFinalList.append(myList[i + 2])
            myFinalList.append(myList[i])
        if(j == 1):
            myFinalList.append(myList[j])
            myFinalList.append(myCopiedList[j])
            myFinalList.append(myCopiedList1[j])
        j += 1
        
    print("Here is my final list:",myFinalList)
    
    finLenList = len(myFinalList)
    
    i = 0
    counter = 0
    for i in range(finLenList):
        print(myFinalList[i], end= " ")
        counter += 1
        
        if(counter == 3):
            print("\n")
            counter = 0
