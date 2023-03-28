
def printBoard(xState, zStategit ):
    zero  = 'X' if xState[0] else ('O' if zState[0] else 0)
    one   = 'X' if xState[1] else ('O' if zState[1] else 1)
    two   = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four  = 'X' if xState[4] else ('O' if zState[4] else 4)
    five  = 'X' if xState[5] else ('O' if zState[5] else 5)
    six   = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    pass

if __name__ =="__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn =1 #1 for x and 0 for o
    print("Welcome to TIC TAC TOE")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print()
            print("X's CHANCE")
            value = int(input("Please Enter a value: "))
            xState[value] = 1
        else:
            print()
            print("0's CHANCE")
            value = int(input("Please Enter a value: "))
            zState[value] = 1
        turn = 1-turn
        