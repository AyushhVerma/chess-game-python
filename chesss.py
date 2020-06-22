print(r''' 
┌──┐┐  ┌ ┌──┐┌──┐ ┌──┐	┌──┐┌──┐ ┌──┐┌──┐ ┌──┐
│   ├──┤ ├── └──┐ └──┐	│ ─┐├──┤ │  ││  │ ├── 
└──┘┘  └ └──┘└──┘ └──┘	└──┘┘  └ ┘  └┘  └ └──┘
''')		
board={ '1':["BR │","BN │","BB │","BQ │","BK │","BB │","BN │","BR │"],
		'2':["BP │","BP │","BP │","BP │","BP │","BP │","BP │","BP │"],
		'3':["   │","   │","   │","   │","   │","   │","   │","   │"],
		'4':["   │","   │","   │","   │","   │","   │","   │","   │"],
		'5':["   │","   │","   │","   │","   │","   │","   │","   │"],
		'6':["   │","   │","   │","   │","   │","   │","   │","   │"],
		'7':["WP │","WP │","WP │","WP │","WP │","WP │","WP │","WP │"],
		'8':["WR │","WN │","WB │","WQ │","WK │","WB │","WN │","WR │"]}
replace={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7} 
turn=["P1","P2"]
l=[]
def print_board():
    print("   a    b    c    d    e    f    g    h")
    print(" ┌────┬────┬────┬────┬────┬────┬────┬────┐")
    j=1
    for i in board.values():
        print(str(j)+"│",*(i),str(j))
        j+=1
        if j<9:
            print(" ├────┼────┼────┼────┼────┼────┼────┼────┤" )
    print(" └────┴────┴────┴────┴────┴────┴────┴────┘")
    print("   a    b    c    d    e    f    g    h")
    print("\n*PLAYER 1 plays WHITE & PLAYER 2 plays BLACK.*")
        
print_board()
print(" START GAME ".center(42,"*"))
print(r" [ 'B': Black,  'W': White ]  ['R': Rook, 'N': Knight, 'B': Bishop, 'Q': Queen, 'K': King,'P': Pawn]")

def change_piece_position(move):
	board[move[5]][replace[move[4]]]=board[move[3]][replace[move[2]]]
	board[move[3]][replace[move[2]]]="   │"

def invalid_function_call():
	print("invalid move ,try again")

def pawn_move(move,s1,s2,enpass):
	if (move[:2]==s1+"P") and ((s1=="W" and ((int(move[3])>int(move[5])))) or (s1=="B" and (int(move[3])<int (move[5])))):	
		if ((move[2] is move[4]) and (abs(int(move[3])-int(move[5]))==1)and (board[move[5]][replace[move[4]]][0] in (' '))) \
		or (abs(replace[move[2]]-replace[move[4]])==1 and ((board[move[5]][replace[move[4]]][0]==s2))):
			change_piece_position(move)
			check_pawn_promotion(move,s1)
			return True,' '
		elif (move[2] is move[4]) and (abs(int(move[3])-int(move[5]))==2) and ((s1=="W" and move[3]=="7" )or (s1=="B" and move[3]=="2") and inline_move(move,s2)) :
			change_piece_position(move)
			return True,(move[4]+'3' if s1=='B' else (move[4]+'6'))
		if (abs(replace[move[2]]-replace[move[4]])==1 and (board[move[5]][replace[move[4]]][0]==' ')) \
		and move[-2:]== enpass:
			change_piece_position(move)
			board[move[3]][replace[move[4]]]='   │'
			return True, ' '
	invalid_function_call()
	return False,' ' 
	
def check_pawn_promotion(move,s1):
	if (s1 == "W" and move[-1]=='1'):
		pawn_promotion("w",move[-2:])
	elif (s1 == "B" and move[-1]=='8'):
		pawn_promotion("b",move[-2:])

def pawn_promotion(promote,at):
	new=input("['R' for Rook, 'N' for Knight, 'B' for Bishop, 'Q' for Queen]").upper()
	if new not in ('R','N','Q','B'):
		print("enter valid piece")
	elif promote == 'b':
		board[at[1]][replace[at[0]]]="B"+new+" │"
	else:
		board[at[1]][replace[at[0]]]="W"+new+" │"
				
def king_move(move,s1,s2):			
	if move[:2]==s1+"K" and (abs(replace[move[2]]-replace[move[4]]) or abs(int(move[3])-int(move[5]))==1) and (board[move[5]][replace[move[4]]][0]in (s2,' ')):
		change_piece_position(move)
		return True
	invalid_function_call()
	return False
	
def rook_move(move,s1,s2):
	if (move[:2]==s1+"R") and inline_move(move,s2):
		change_piece_position(move)
		return True
	invalid_function_call()
	return False

def clear_inline_move(move):
	i,i1=(min(int(move[3]),int(move[5]))+1),min(replace[move[2]],replace[move[4]])+1
	j,j1=max(int(move[3]),int(move[5])),max(replace[move[2]],replace[move[4]])
	while i<j:
		if board[str(i)][replace[move[2]]][0] is not ' ':
			return False
		i+=1
	while i1<j1:
		if board[move[3]][i1][0]!=' ':
			return False
		i1+=1
	return True

def inline_move(move,s2):
	return (((move[2] == move[4]) or (move[3] == move[5])) and (board[move[5]][replace[move[4]]][0] in(" ",s2)) and (clear_inline_move(move)))

def queen_move(move,s1,s2):
	if(move[:2]==s1+"Q") and (diagonal_move(move,s2) or inline_move(move,s2)):
		change_piece_position(move)
		return True
	invalid_function_call()
	return False

def bishop_move(move,s1,s2):
	if (move[:2]==s1+"B") and diagonal_move(move,s2):
		change_piece_position(move)
		return True
	invalid_function_call()
	return False

def clear_diagonal_move(move):
	i,i1=min(int(move[3]),int(move[5]))+1,min(replace[move[2]],replace[move[4]])+1	
	j,j1=max(int(move[3]),int(move[5])),max(replace[move[2]],replace[move[4]])
	while i<j:
		if board[str(i)][i1][0]!= ' ':
			return False
		i+=1
		i1+=1
	return True

def diagonal_move(move,s2):
	return (abs(replace[move[2]]-replace[move[4]]) == abs(int(move[3])-int(move[5])))>0 and (board[move[5]][replace[move[4]]][0] in (s2,' ') and (clear_diagonal_move(move)) )

def knight_move(move,s1,s2):
	if (move[:2]==s1+"N") and ((abs(replace[move[2]]-replace[move[4]]),abs(int(move[3])-int(move[5])))is (1,2) or (2,1)) and (board[move[5]][replace[move[4]]][0]in (s2,' ')):
		change_piece_position(move)
		return True
	invalid_function_call()
	return False

def update_castling_check(position,check=' '):
	l.append(position)
	return check not in l

def castling_p1(move,s1,s2,castling):
	if clear_inline_move(move) and update_castling_check('$',check=board[move[-1]][replace[move[-2]]][:2])and castling and  move[4]=='H':
		if not(function_for_check('G1',"W","B")):
			return True
	elif clear_inline_move(move) and update_castling_check('$',check=board[move[-1]][replace[move[-2]]][:2])and castling and  move[4]=='A':
		if not(function_for_check('C1',"B","W")):
			return True
	return False

def castling_p2(move,s1,s2,castling):
	if clear_inline_move(move) and update_castling_check('$',check=board[move[-1]][replace[move[-2]]][:2])and castling and  move[4]=='H':
		if not(function_for_check('G8',"B","W")):
			return True
	elif clear_inline_move(move) and update_castling_check('$',check=board[move[-1]][replace[move[-2]]][:2])and castling and  move[4]=='A':
		if not(function_for_check('C8',"B","W")):
			return True
	return False

def castle_move(change,at):
	if at=='1':
		board[at][4-change]="BK │"
		board['1'][4]="   │"
		if change>1:
			board[at][3]="BR │"
			board[at][0]="   │"
		else:
			board[at][5]="BR │"
			board[at][7]="   │"
	else:
		board[at][4-change]="WK │"
		board['1'][4]="   │"
		if change>1:
			board[at][3]="WR │"
			board[at][0]="   │"
		else:
			board[at][5]="WR │"
			board[at][7]="   │"

def function_for_check(pos,s1,s2):
	i,j=replace[pos[0]]+1,pos[1]
	while i<=7:
		if board[j][i][0]==s1:
			break
		elif board[j][i][1] in ('R','Q'):
			return True,[i,j,'I']
		i+=1
	i,j=replace[pos[0]]-1,pos[1]
	while i>=0:	
		if board[j][i][0]==s1:
			break
		elif board[j][i][1] in ('R','Q'):
			return True,[i,j,'I']
		i-=1
	i,j=replace[pos[0]],int(pos[1])+1
	while j<=8:	
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('R','Q'):
			return True,[i,j,'I']
		j+=1
	i,j=replace[pos[0]],int(pos[1])-1
	while j>=1:	
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('R','Q'):
			return True,[i,j,'I']
		j-=1
	i,j=replace[pos[0]],int(pos[1])
	l=[[2,-1],[2,1],[1,2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2]]
	for x,y in l:
		if (i+x) in range(8) and (y+j)in range(1,9) :
			if board[str(j+y)][i+x][:2]==s2+'N':
				return True,[i,j,'N']
	i,j=replace[pos[0]],int(pos[1])
	if s1=='W' and (board[str(j-1)][i+1][:2] or board[str(j-1)][i-1][:2])==s2+"P":
		return True,[i,j,'P']
	elif s1=="B" and (board[str(j+1)][i+1][:2] or board[str(j+1)][i-1][:2])==s2+"P":
		return True,[i,j,'P']
	i,j=replace[pos[0]]+1,int(pos[1])+1
	while i<=7 and j<=8:
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('B','Q'):
			return True,[i,j,'D']
		i,j=i+1,j+1
	i,j=replace[pos[0]]-1,int(pos[1])-1
	while i>=0 and j>=1:
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('B','Q'):
			return True,[i,j,'D']
		i,j=i-1,j-1
	i,j=replace[pos[0]]-1,int(pos[1])+1
	while i>=0 and j<=8:
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('B','Q'):
			return True,[i,j,'D']
		i,j=i-1,j+1
	i,j=replace[pos[0]]+1,int(pos[1])-1
	while i<=7 and j>=1:
		if board[str(j)][i][0]==s1:
			break
		elif board[str(j)][i][1] in ('B','Q'):
			return True,[i,j,'D']
		i,j=i+1,j-1
	return False,[]

def function_for_checkmate(king,s2,s1,pos):
	i,j=pos[:2]
	if pos[2]=='D':
		a,b=replace[king[0]],int(king[1])
		if a<i and b>j:
			while a<=i and b>=j:
				a,b=a+1,b-1
				if function_for_check(str(a)+str(b),s2,s1) or (s2=="W" and a!=i and ((b==5 and board[str(a+2)][b][:2]=="WP" or board[str(a+1)][b][:2]=="WP"))) or \
				  (s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False
		elif a<i and b<j:
			while a<=i and b<=j:
				a,b=a+1,b+1
				if function_for_check(str(a)+str(b),s2,s1) or (s2=="W" and a!=i and ((b==5 and board[str(a+2)][b][:2]=="WP" or board[str(a+1)][b][:2]=="WP"))) or \
				(s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False
		elif a>i and b<j:
			while a>=i and b<=j:
				a,b=a-1,b+1
				if function_for_check(str(a)+str(b),s2,s1) or (s2=="W" and a!=i and ((b==5 and board[str(a+2)][b][:2]=="WP" or board[str(a+1)][b][:2]=="WP"))) or \
				  (s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False			
		elif a>i and b>j:
			while a>=i and b>=j:
				a,b=a-1,b-1
				if function_for_check(str(a)+str(b),s2,s1) or (s2=="W" and a!=i and ((b==5 and board[str(a+2)][b][:2]=="WP" or board[str(a+1)][b][:2]=="WP"))) or \
				(s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False
		return True
	elif pos[2]=='I':
		a,b=replace[king[0]],int(king[1])
		if a>i and b==j:
			while a>=i:
				a-=1
				if function_for_check(str(a)+str(b),s2,s1) or(s2=='W'and a!=i and((b==5 and board[str(b+2)][a][:2]=="WP") or (board[str(b+1)][a][:2]=="WP")))\
				or (s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False
		elif a<i and b==j:
			while a<=i:
				a+=1
				if function_for_check(str(a)+str(b),s2,s1) or (s2=='W'and a!=i and((b==5 and board[str(b+2)][a][:2]=="WP") or (board[str(b+1)][a][:2]=="WP")))\
				or (s2=='B'and a!=i and((b==2 and board[str(b-2)][a][:2]=="BP") or (board[str(b-1)][a][:2]=="BP"))):
					return False
		elif a==i and b<j:
			while b<=j:
				b+=1
				if function_for_check(str(a)+str(b),s2,s1) :
					return False
		elif a==i and b>j:
			while a>=i: 
				b-=1
				if function_for_check(str(a)+str(b),s2,s1) :
					return False            
	elif pos[2]=='P' and function_for_check(str(pos[0])+str(pos[1]),s2,s1):
		return False
	elif pos[2]=='N' and function_for_check(str(pos[0])+str(pos[1]),s2,s1):
		return False
	return True

def king_check_move(pos,s1,s2):
	i,j=replace[pos[0]],int(pos[0])
	l=[[1,1],[-1,-1],[1,0],[0,1],[-1,0][0,-1][1,-1],[-1,1]]
	for x,y in l:
		if (i+x) in range(8) and (y+j)in range(1,9):
			if (board[str(j+y)][i+x][0]=='W') and (function_for_check(str(x+i)+str(y+j),s1,s2)):
				return False
	return True

def Game_Start():
	check,k=False,0
	castle_White_left,castle_White_right="WKE8H8","WKE8A8"
	castle_Black_left,castle_Black_right="BKE1H1","BKE1A1"
	castling_black=castling_white=True
	enpass= ' '
	king_position=['E8','E1']
	while True:
		(s1,s2)=(("W","B") if k%2==0 else ("B","W"))
		if castling_white and turn[k%2]==0:
			print(r"For Castling input format: wke8(h8,a8) or bke1(h1,a1) ")
		elif castling_black and turn[k%2]:
			print(r"For Castling input format: wke8(h8,a8) or bke1(h1,a1) ")
		next_move=True
		print(turn[k%2]+"'s turn")
		entered_move=input().upper()
		piece=entered_move[1]
		if entered_move[0] is not s1:
			continue
		if (len(entered_move)!=6) or ((entered_move[2]and entered_move[4]) not in replace.keys())\
		or(int((entered_move[3]) and int(entered_move[5]))not in range(1,9))or (piece not in ('P','Q','R','K','B','N')):
			print("out of bound input")
			continue			
		elif (entered_move[:2] != board[entered_move[3]][replace[entered_move[2]]][:2]):
			print(r"Error: No Pawn Here,invalid input")
			continue
		elif (entered_move in (castle_White_left,castle_White_right)):
			if castling_p1(entered_move,s1,s2,castling_white):
				castle_move((replace[move[2]]-replace[move[4]])//2,'8')
			enpass=' '
		elif (entered_move in (castle_Black_left,castle_Black_right)):
			if castling_p2(entered_move,s1,s2,castling_black):
				castle_move((replace[move[2]]-replace[move[4]])//2,'8')
			enpass=' '
		elif piece is "P": 
			next_move,enpass=pawn_move(entered_move,s1,s2,enpass)
			if next_move==False:
				continue
		elif piece is "K":
			if abs(int(entered_move[-1])-int(king_position[(k+1)%2][1]))>1\
			or abs(replace[entered_move[-2]]-replace[king_position[(k+1)%2][0]])>1:
				next_move=king_move(entered_move,s1,s2)
				if next_move==False:
					continue
				king_position[k%2]=entered_move[-2:]
				if k%2==0:
					castling_white=False
				else:
					castling_black=False
				enpass=' '
			else:
				print("KING can't move there")
				continue
		elif piece is "R":
			next_move=rook_move(entered_move,s1,s2)
			if next_move==False:
				continue
			update_castling_check(entered_move[:2],check=' ')
			enpass=' '
		elif piece is "B":
			next_move=bishop_move(entered_move,s1,s2)
			if next_move==False:
				continue
			enpass=' '	
		elif piece is "Q":
			next_move=queen_move(entered_move,s1,s2)
			if next_move==False:
				continue
			enpass=' '	
		elif piece is "N":
			next_move=knight_move(entered_move,s1,s2)
			if next_move==False:
				continue
			enpass=' '
		check,pos=function_for_check(king_position[k%2],s1,s2)
		if check:
			print("King will be in check ,can't move there")
			change_piece_position(entered_move[:2]+entered_move[4:]+entered_move[2:4])
			continue
		k+=1
		check,pos=function_for_check(king_position[k%2],s2,s1)
		if check:
			checkmate= function_for_checkmate(king_position[k%2],s2,s1,pos) or king_check_move(king_position[k%2],s2,s1) \
			or (((castling_p1("WKE8H8","W","B",castling_white)) or (castling_p1("WKE8A8","W","B",castling_white))) if k%2==0 else \
			((castling_p2("BKE1H1","B","W",castling_black)) or (castling_p2("BKE1A1","B","W",castling_black)))) 
			if (not checkmate):
				print(" Checkmate... ,%s wins "%turn[k%2])
				break
			print(" Check! ")
		print_board()
	print("Number of turns to victory: %s"%(k//2))

Game_Start()
