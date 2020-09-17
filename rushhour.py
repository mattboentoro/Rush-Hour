import copy
class BoardState:
    #container for board state
    def __init__(self):
        self.board=[[]]
        self.parent=[]
        self.symbol=[]
        self.heuristic=0
        self.gn=0
        self.fn=0
    def print(self):
        #for debugging purposes
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j],end=' ')
            print()
        print()
    def heuristiczero(self):
        #first heuristic
        #blocking car heuristic
        if(self.board[2][5]=="X"):
            self.fn=0
        else:
            arr=[]
            for i in range(len(self.board[2])):
                if((self.board[2][i]!="X")&(self.board[2][i]!="-")&(self.board[2][i] not in arr)):
                    arr.append(self.board[2][i])
            self.fn=1+len(arr)
    def heuristicone(self):
        #second heuristic
        #blocking car heuristic + X distance from the end
        #it is as effective as the blocking car heuristic since it also weigh in the distance of the car into the exit
        if(self.board[2][5]=="X"):
            self.fn=0
        else:
            arr=[]
            index=-1
            for i in range(len(self.board[2])):
                if((self.board[2][i]!="X")&(self.board[2][i]!="-")&(self.board[2][i] not in arr)):
                    arr.append(self.board[2][i])
                if(self.board[2][i]=="X"):
                    index=i
            self.fn=(5-index)+((len(arr))*5)
class Car:
    #container for the cars in the board
    def __init__(self):
        self.symbol=""
        self.size=0
        self.orientation=""
        self.start_i=-1
        self.start_j=-1
    def print(self):
        #print debugging purposes
        print(self.symbol)
        print(self.size)
        print(self.orientation)
        print("Start i: "+str(self.start_i))
        print("Start j: "+str(self.start_j))
def countsymbol(array,symbol):
    #count how many symbols are there in the board
    #array = 2d-array of characters
    #symbol= characters to be searched
    count=0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(array[i][j]==symbol):
                count+=1
    return count
def getsymbol2(array,cararray):
    #get the symbol, length, size, orientation from the board
    #array = 2-d array of characters
    #cararray = previous car list instances
    tokens=[]
    symbol=[]
    car=Car()
    for i in range(len(array)):
        for j in range(len(array[i])):
            if((array[i][j]!="-")&(array[i][j] not in tokens)):
                token=array[i][j]
                tokens.append(token)
                car.symbol=token
                car.start_i=i
                car.start_j=j
                if(j+1<len(array[i])):
                    if(array[i][j+1]==token):
                        car.orientation="horizontal"
                    else:
                        car.orientation="vertical"
                else:
                    car.orientation="vertical"
                for instance in cararray:
                    if(instance.symbol==token):
                        car.size=instance.size
                symbol.append(copy.deepcopy(car))
    return symbol

def getsymbol(array):
    #get the symbol, length, size, orientation from the board
    #array = 2-d array of characters
    tokens=[]
    symbol=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if((array[i][j]!="-")&(array[i][j] not in tokens)):
                token=array[i][j]
                tokens.append(token)
                car=Car()
                car.symbol=token
                car.start_i=i
                car.start_j=j
                if(j+1<len(array[i])):
                    if(array[i][j+1]==token):
                        car.orientation="horizontal"
                    else:
                        car.orientation="vertical"
                else:
                    car.orientation="vertical"
                car.size=countsymbol(array,token)
                symbol.append(copy.deepcopy(car))
    return symbol
def possiblemoves(boardstate):
    #return array of possible moves represented in BoardState class instances
    #boardstate = instance of BoardState class
    arr=[]
    array=boardstate.board
    heuristic=boardstate.heuristic
    for i in boardstate.symbol:
        if(i.orientation=="vertical"):
            if((i.start_i-1)>=0):
                if(array[i.start_i-1][i.start_j]=="-"):
                    newboard=BoardState()
                    newboard.parent=copy.deepcopy(array)
                    newboard.board=copy.deepcopy(array)
                    newboard.board[i.start_i-1][i.start_j]=i.symbol
                    newboard.board[i.start_i+i.size-1][i.start_j]="-"
                    newboard.symbol=getsymbol2(newboard.board,boardstate.symbol)
                    newboard.gn=boardstate.gn+1
                    if(heuristic==0):
                        newboard.heuristic=0
                        newboard.heuristiczero()
                    else:
                        newboard.heuristic=1
                        newboard.heuristicone()
                    arr.append(newboard)
            if(i.start_i+i.size<=len(array)-1):
                if(array[i.start_i+i.size][i.start_j]=="-"):
                    newboard=BoardState()
                    newboard.parent=copy.deepcopy(array)
                    newboard.board=copy.deepcopy(array)
                    newboard.board[i.start_i+i.size][i.start_j]=i.symbol
                    newboard.board[i.start_i][i.start_j]="-"
                    newboard.symbol=getsymbol2(newboard.board,boardstate.symbol)
                    newboard.gn=boardstate.gn+1
                    if(heuristic==0):
                        newboard.heuristic=0
                        newboard.heuristiczero()
                    else:
                        newboard.heuristic=1
                        newboard.heuristicone()
                    arr.append(newboard)
        else:
            if(i.start_j-1>=0):
                if(array[i.start_i][i.start_j-1]=="-"):
                    newboard=BoardState()
                    newboard.parent=copy.deepcopy(array)
                    newboard.board=copy.deepcopy(array)
                    newboard.board[i.start_i][i.start_j-1]=i.symbol
                    newboard.board[i.start_i][i.start_j+i.size-1]="-"
                    newboard.symbol=getsymbol2(newboard.board,boardstate.symbol)
                    newboard.gn=boardstate.gn+1
                    if(heuristic==0):
                        newboard.heuristic=0
                        newboard.heuristiczero()
                    else:
                        newboard.heuristic=1
                        newboard.heuristicone()
                    arr.append(newboard)
            if(i.start_j+i.size<=len(array)-1):
                if(array[i.start_i][i.start_j+i.size]=="-"):
                    newboard=BoardState()
                    newboard.parent=copy.deepcopy(array)
                    newboard.board=copy.deepcopy(array)
                    newboard.board[i.start_i][i.start_j+i.size]=i.symbol
                    newboard.board[i.start_i][i.start_j]="-"
                    newboard.symbol=getsymbol2(newboard.board,boardstate.symbol)
                    newboard.gn=boardstate.gn+1
                    if(heuristic==0):
                        newboard.heuristic=0
                        newboard.heuristiczero()
                    else:
                        newboard.heuristic=1
                        newboard.heuristicone()
                    arr.append(newboard)
    return arr
def insertionsort(arr):
    #sort the array
    #arr = list of BoardState class instances
    for i in range(len(arr)):
        cursor=arr[i]
        pos=i
        while (pos>0 and ((arr[pos-1].fn+arr[pos-1].gn)>(cursor.fn+cursor.gn))):
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=cursor
    return arr
def rushhour(heuristic,array):
    mainarray=[] #list of unexplored
    explored=[] #list of explored states
    mainarraysupp=[] #list of 2d array of the board only
    arr=[] #list of 2d array from the representation
    for i in array:
        arr.append([char for char in i]) #split into 2d array to make it more accessible
    state=BoardState()
    state.board=copy.deepcopy(arr)
    state.symbol=getsymbol(arr)
    state.heuristic=heuristic
    if(heuristic==0):
        state.heuristiczero()
    else:
        state.heuristicone()
    mainarray.append(state)
    mainarraysupp.append(arr)
    while (len(mainarray)>0):
        currentstate=mainarray.pop(0) #BoardState instance
        explored.append(currentstate)
        if(currentstate.fn==0):
            mainarraysupp.append(currentstate.board)
            break
        moves=possiblemoves(currentstate)
        for i in moves:
            if i.board not in mainarraysupp:
                mainarray.append(i)
                mainarraysupp.append(i.board)
        mainarray=insertionsort(mainarray)
    result=[]
    result.append(explored[len(explored)-1])
    parent=explored[len(explored)-1].parent
    while (parent!=[]):
        index=-1
        for i in range(len(explored)):
            if (explored[i].board==parent):
                index=i
        result.append(explored[index])
        parent=explored[index].parent
    for i in range(len(result)-1,-1,-1):
        result[i].print()
    print("Total moves: "+str(len(result)-1))
    print("Total states explored: "+str(len(explored)+len(mainarray)))

            
rushhour(1,["--C---","--C---","XXC---","--ZZ--","------","------"])
#rushhour(0,["------","------","XXX---","--Y---","--Y---","------"])
#rushhour(0,["----O-","-PPPO-","XXA-O-","--ADD-","QQQG--","---G--"])
#rushhour(0,["AKKI--","A--I--","XXO---","--OPPP","--O--D","--QQQD"])
#rushhour(0,["MMMDEF","ANNDEF","A-XXEF","PPC---","-BC-QQ","-BRRSS"])
#rushhour(0,["AKKI--","A--I--","XXO---","--OPPP","--O--D","--QQQD"])
#rushhour(0,["ABB---","A--C--","AXXC--","D--C-F","D----F","--EEEF"])
