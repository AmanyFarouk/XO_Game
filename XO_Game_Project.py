#function for printing the list
def Printing(list):
    print("--------------")
    for x in list:
        print("|",end=" ")
        for y in x:
            print(y,"|",end=" ")
        print("\n--------------")
#function that checks if any player win
def winPlayer(list,char):
    countDiag=0
    for i in range(len(list)):
        countRow=0
        for j in range(len(list)):
            #for the diagonal
            if i==j and i!=0:
                if list[i][j]==list[i-1][j-1] and list[i][j]==char:
                    countDiag+=1
            # check for row
            elif j!=0 :
                if list[i][j]==list[i][j-1] and list[i][j]==char:
                    countRow+=1

        if countDiag==2 :
            return True
        elif countRow==2:
            return True
    for j in range(len(list)):
        countCol=0
        for i in range(len(list)):
            #check for column
            if i!=0:
                if list[i][j]==list[i-1][j] and list[i][j]==char:
                    countCol+=1
                    if countCol==2:
                        return True
        #check the second diagonal
        if list[0][2]==list[1][1]==list[2][0]and list[1][1]==char:
            return True
    return False
#function for inserting to the list
def insert (list,num,char):
    #if the number 1 or 2 or 3 in the first row
    if num-1<3:
        list[0][num-1]=char
    #if the number 4 or 5 or 6 in the second row
    elif num-1<6:
        list[1][num-4]=char      
    #if the number 7 or 8 or 9 in the last row
    elif num-1<9:
        list[2][num-7]=char
#function that checks if the number if valid , the position is empty '-'
def Check_Validation(list,num):
    if num-1<3:
        if list[0][num-1]=='-':
            return True
        return False
    elif num-1<6:
        if list[1][num-4]=='-':
            return True
        return False
    elif num-1<9:
        if list[2][num-7]=='-':
            return True 
        return False
#create an empty list 3x3
list=[['-','-','-'],['-','-','-'],['-','-','-']]
#countplays to count the number of plays that plays the two players
countPlays=0
while True:
    #player1 is X and player2 is O
    if countPlays%2==0 and countPlays<9:
        player1=int(input("player1 please enter your number: "))
        if 0<player1<10:
            if Check_Validation(list,player1):
                insert(list,player1,'X')
                countPlays+=1
            else:
                print("this position is filled try another potition")
                continue
            if winPlayer(list,'X'):
                print("player1 wins")
                Printing(list)
                break
            else:
                Printing(list)
        else :
            print("the number you entered out of range")
            continue
    if countPlays%2!=0 and countPlays<9:
        player2=int(input("player2 please enter your number: "))
        if 0<player2<10:
            if Check_Validation(list,player2):
                insert(list,player2,'O')
                countPlays+=1
            else:
                print("this position is filled try another potition")
                continue
            if winPlayer(list,'O'):
                print("player2 wins")
                Printing(list)
                break
            else:
                Printing(list)
        else:
            print("the number you entered out of range")
            continue
    if countPlays==9:
        print("Tie")
        break