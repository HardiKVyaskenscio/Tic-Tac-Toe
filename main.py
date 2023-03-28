
def printBoard():
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"3 | 4 | 5 ")
    print(f"--|---|---")
    print(f"9 | 7 | 8 ")
    pass

if __name__ =="__main__":
    xState = [0,0,0,0,0,0,0,0]
    yState = [0,0,0,0,0,0,0,0]
    turn =1 #1 for x and 0 for o
    print("Welcome to TIC TAC TOE")
    while(True):
        printBoard()
        if(turn == 1):
            print("X's CHANCE")
            value = int(input("Please Enter a value: "))
            xState[value] = 1
        else:
            
            print("X's CHANCE")
            value = int(input("Please Enter a value: "))
            zState[value] = 1
        
        break