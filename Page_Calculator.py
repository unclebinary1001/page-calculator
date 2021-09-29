class SheetA4 :
    def __init__ (self):
        self.FrontPhysical = [0] *4
        self.BackPhysical = [0] *4
    

class SheetA5Horizontal :
    def __init__(self):    
        self.FrontPhysical = [0]*2
        self.BackPhysical = [0]*2
    
def main():
    
    nPages = int(input("Enter number of pages - must be multiple of 8:\n"))
    
    #Check of nPages is a multiple of 8
    if (nPages%8!=0):
        print("Number of pages - must be multiple of 8!!!")
        return
    
    #Create physicalA4 sheets and numner the physical A6 pages on them
    nSheets = nPages//8
    
    sheetsA4 = []
    for i in range(nSheets):
        sheetsA4.append(SheetA4())

    curPage = 1
    
    #Number all a4 sheets
    for n in range(0, nSheets):
        
        #Front
        sheetsA4[n].FrontPhysical[0]=curPage
        curPage+=1
        #1,9,17
        
        sheetsA4[n].FrontPhysical[1]=curPage
        curPage+=1
        #2,10,18
        sheetsA4[n].FrontPhysical[2]=curPage
        curPage+=1
        #3,11,19
        sheetsA4[n].FrontPhysical[3]=curPage
        curPage+=1
        #4,12,20
        #Back
        sheetsA4[n].BackPhysical[0]=curPage
        curPage+=1
        #5,13,21
        sheetsA4[n].BackPhysical[1]=curPage
        curPage+=1
        #6,14,22
        sheetsA4[n].BackPhysical[2]=curPage
        curPage+=1
        #7,15,23
        sheetsA4[n].BackPhysical[3]=curPage
        curPage+=1
        #8,16,24
    #Rip in half horizontally
    sheetsA5 = []
    size = nSheets * 2
    for i in range(size):
        sheetsA5.append(SheetA5Horizontal())
    
    #Top half
    
    
    for n in range(0, nSheets):
        
        #Front
        sheetsA5[n].FrontPhysical[0]= sheetsA4[n].FrontPhysical[0]
        
        sheetsA5[n].FrontPhysical[1]= sheetsA4[n].FrontPhysical[1]
        
        #Back
        sheetsA5[n].BackPhysical[0]= sheetsA4[n].BackPhysical[0]
        
        sheetsA5[n].BackPhysical[1]= sheetsA4[n].BackPhysical[1]

    
    #Bottom half
    for n in range(0, nSheets):
        #Front
        sheetsA5[nSheets+n].FrontPhysical[0]= sheetsA4[n].FrontPhysical[2]
        
        sheetsA5[nSheets+n].FrontPhysical[1]= sheetsA4[n].FrontPhysical[3]
        
        #Back
        sheetsA5[nSheets+n].BackPhysical[0]= sheetsA4[n].BackPhysical[2]
        
        sheetsA5[nSheets+n].BackPhysical[1]= sheetsA4[n].BackPhysical[3]
        

    #Numnber all physical pages in book order
    curPage = 0
    bookOrder =[0] * nPages
    
    #Left pages of the stack going up = first half book pages
    for n in range(0, len(sheetsA5)):
        
        #Back right
        bookOrder[curPage] = sheetsA5[n].BackPhysical[1]
        curPage+=1

        #Front left
        bookOrder[curPage] = sheetsA5[n].FrontPhysical[0]
        curPage+=1
        

    #Right pages of the stack going down = second half book pages
    for n in range(len(sheetsA5)-1, -1, -1):
        
        #Front right
        bookOrder[curPage] = sheetsA5[n].FrontPhysical[1]
        
        curPage+=1

        #Back left
        bookOrder[curPage] = sheetsA5[n].BackPhysical[0]
        curPage+=1
        

    
    printOrder = [0] * nPages
    for index in range(0,len(bookOrder)):
        printOrder[bookOrder[index]-1] = index+1

    #print result
    print("Number of sheets of paper", nSheets)
    print("print order:", printOrder)
    
    num = input("Press any key to exit: ")
    
main()
