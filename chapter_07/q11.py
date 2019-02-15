# Lo Shu Magic Square

ROWS = 3
COLS = 3
def main():
    # create a two dimensional list
    square = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    # ask the user to enter values to fill the list
    user_numbers = []
    index = 0
    while index < 9:   
        value = int(input("Enter a number from 1 through 9: "))
        if value >=1 and value <= 9 and value not in user_numbers:
            print("Success")
            user_numbers.append(value)
            index += 1
            
        else:
            print("Your number is already entered or it is not in range 1-9. Please enter again.")
            
    # user_numbers list is one-dimensional. convert to two dimensional list
    index2 = 0
    for r in range(ROWS):
        for c in range(COLS):
            square[r][c] = user_numbers[index2]
            index2 += 1
            
    print()
    
    # display the user's two-dimensional list
    print("Your two-dimensional list is below")
    for r in range(ROWS):
        for c in range(COLS):
            print(square[r][c], end="\t")
        print()
        
# get the totals from functions and assign them to variables    
    row1,row2,row3=SumofRows(square)
    col1,col2,col3=SumofCols(square)    
    diag1,diag2=SumofDiagonal(square)
    
    # compare them if they are equal.
    if row1==row2==row3==col1==col2==col3==diag1==diag2:
        print("It is a Lo Shu Magic Square.")
    else:
        print("It is not a Lo Shu Magic Square.")
 
def SumofRows(square):
    totalrow1=0
    for c in range(COLS):
        totalrow1+=square[0][c-1]
    totalrow2=0
    for c in range(COLS):
        totalrow2+=square[1][c-1]
    totalrow3=0
    for c in range(COLS):
        totalrow3+=square[2][c-1]
    return totalrow1, totalrow2, totalrow3

def SumofCols(square):
    totalcol1=0
    for r in range(ROWS):
        totalcol1+=square[r-1][0]
    totalcol2=0
    for r in range(ROWS):
        totalcol2+=square[r-1][1]
    totalcol3=0
    for r in range(ROWS):
        totalcol3+=square[r-1][2]    
    return totalcol1,totalcol2,totalcol3

def SumofDiagonal(square):
    # calculate manually
    first_diag=square[0][0] + square[1][1] + square[2][2]
    second_diag=square[0][2] + square[1][1] + square[2][0]
    return first_diag, second_diag    
        
# call the main function.
main()
    
    