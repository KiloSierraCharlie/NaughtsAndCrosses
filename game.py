from random import choice

A = [None]*3;
A[0] = " ";
A[1] = " ";
A[2] = " ";

B = [None]*3;
B[0] = " ";
B[1] = " ";
B[2] = " ";

C = [None]*3;
C[0] = " ";
C[1] = " ";
C[2] = " ";

PLAYER = 0;
COMPUT = 1;

WinningPatterns = [
  # Horizontal              
  ["A1", "A2", "A3"],
  ["B1", "B2", "B3"],
  ["C1", "C2", "C3"],
  # Diagonals
  ["A1", "B2", "C3"],
  ["A3", "B2", "C1"],
  # Verticals
  ["A1", "B1", "C1"],
  ["A2", "B2", "C2"],
  ["A3", "B3", "C3"]
];

def DrawGrid( ):
    print( "\n" * 1000 );
    print(A[0] + "|" + A[1] + "|" + A[2]);
    print("-" * 5);
    print(B[0] + "|" + B[1] + "|" + B[2]);
    print("-" * 5);
    print(C[0] + "|" + C[1] + "|" + C[2]);
    print( "\n" * 2 );
    
def SetMovePos( reqPos, WHO ):
    Marker = "O";
    WHOTXT = "Computer";
    if( WHO == PLAYER ):
        Marker = "X";
        WHOTXT = "Player";
    if( len( reqPos ) == 2 ):
        if( reqPos[0] in ["A", "B", "C"] ):
            if( reqPos[1] in ["1", "2", "3"] ):
                if( reqPos[0] == "A" ):
                    if( A[ int( reqPos[1] ) - 1 ] == " " ):
                        A[ int( reqPos[1] ) - 1 ] = Marker;
                        DrawGrid();
                        print( WHOTXT + " took A" + reqPos[1] );
                        print( "\n" * 2 );
                        RequestPos( ( PLAYER + COMPUT ) - WHO );
                    else:
                        DrawGrid();
                        print( "That position is already taken!" );
                        print( "\n" * 2 );
                        RequestPos( PLAYER );
                elif( reqPos[0] == "B" ):
                    if( B[ int( reqPos[1] ) - 1 ] == " " ):
                        B[ int( reqPos[1] ) - 1 ] = Marker;
                        DrawGrid();
                        print( WHOTXT + " took B" + reqPos[1] );
                        print( "\n" * 2 );
                        RequestPos( ( PLAYER + COMPUT ) - WHO );
                    else:
                        DrawGrid();
                        print( "That position is already taken!" );
                        print( "\n" * 2 );
                        RequestPos( PLAYER );
                else:
                    if( C[ int( reqPos[1] ) - 1 ] == " " ):
                        C[ int( reqPos[1] ) - 1 ] = Marker;
                        DrawGrid();
                        print( WHOTXT + " took C" + reqPos[1] );
                        print( "\n" * 2 );
                        RequestPos( ( PLAYER + COMPUT ) - WHO );
                    else:
                        DrawGrid();
                        print( "That position is already taken!" );
                        print( "\n" * 2 );
                        RequestPos( PLAYER );

def RequestPos( WHO ):
    LAST = " ";
    CONSECUTIVE = 0;

    for Pattern in WinningPatterns:
        for GRID in Pattern:
            if( GRID[0] == "A" ):
                if( A[int(GRID[1])-1] != " " ):
                    if( LAST != A[int(GRID[1])-1] ):
                        LAST = A[int(GRID[1])-1];
                        CONSECUTIVE = 0;
                    CONSECUTIVE = CONSECUTIVE + 1;
                          
            elif( GRID[0] == "B" ):
                if( B[int(GRID[1])-1] != " " ):
                    if( LAST != B[int(GRID[1])-1] ):
                        LAST = B[int(GRID[1])-1];
                        CONSECUTIVE = 0;
                    CONSECUTIVE = CONSECUTIVE + 1;
            elif( GRID[0] == "C" ):
                if( C[int(GRID[1])-1] != " " ):
                    if( LAST != C[int(GRID[1])-1] ):
                        LAST = C[int(GRID[1])-1];
                        CONSECUTIVE = 0;
                    CONSECUTIVE = CONSECUTIVE + 1;
        if( CONSECUTIVE == 3 ):
            if( LAST == "X" ):
                print("The player has won the game!");
                print("Congratulations!");
                print( "\n" * 1 );
            else:
                print("The computer has won the game!");
                print("Better luck next time!");
                print( "\n" * 1 );
            return;
        CONSECUTIVE = 0;
        
    if( WHO == PLAYER ):
        print( "Use the grid system of A-C on the X axis" );
        print( "And 1-3 on the Y axis," );
        print( "\n" * 1 );
        SetMovePos( input( "Select your next move: " ), PLAYER );
    elif( WHO == COMPUT ):
        USEABLE = [];
        CURRENTTAKEN = [];
        TRY = None;
        for Pattern in WinningPatterns:
            if( TRY != None ):
                USEABLE.append( TRY );
            for GRID in Pattern:
                TRY = Pattern;

                if( GRID[0] == "A" ):
                    if( A[int(GRID[1])-1] == "X" ):
                        TRY = None;
                        break;
                    elif( A[int(GRID[1])-1] == "O" ):
                        CURRENTTAKEN.append( GRID );
                elif( GRID[0] == "B" ):
                    if( B[int(GRID[1])-1] == "X" ):
                        TRY = None;
                        break;
                    elif( B[int(GRID[1])-1] == "O" ):
                        CURRENTTAKEN.append( GRID );
                elif( GRID[0] == "C" ):
                    if( C[int(GRID[1])-1] == "X" ):
                        TRY = None;
                        break;
                    elif( C[int(GRID[1])-1] == "O" ):
                        CURRENTTAKEN.append( GRID );
                        
        if( len( USEABLE ) == 0 ):
            DrawGrid();
            print("The computer has given up!");
            print( "\n" * 1 );
            print("The player has won the game!");
            print("Congratulations!");
            print( "\n" * 1 );
        else:
            CHOICE = choice(choice( USEABLE ));
            while CHOICE in CURRENTTAKEN:
                CHOICE = choice(choice( USEABLE ));
            SetMovePos( CHOICE , COMPUT );
        
DrawGrid();

print( "Welcome to Naughts and Crosses." );
print( "\n" * 2 );

RequestPos( PLAYER );
