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
l1={}
def printboard():										
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
        
printboard()
print(" START GAME ".center(42,"*"))
print(r" [ 'B': Black,  'W': White ]  ['R': Rook, 'N': Knight, 'B': Bishop, 'Q': Queen, 'K': King,'P': Pawn]")

def check_for_check(king,s1,s2):
	i,j=replace[king[0]],int(king[1])
	check=False	
	while i<=7:
		check,k=help_check_inline(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		i+=1
	i,j=replace[king[0]],int(king[1])
	while i>=1:
		check,k=help_check_inline(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		i-=1
	i,j=replace[king[0]],int(king[1])
	while j<=8:
		check,k=help_check_inline(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		j+=1
	i,j=replace[king[0]],int(king[1])
	while j>=1:
		check,k=help_check_inline(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		j-=1
	i,j=replace[king[0]],int(king[1])
	while j<=8 and i<=7:
		check,k=help_check_diagonal(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		j+=1
		i+=1
	i,j=replace[king[0]],int(king[1])
	while j>=1 and i>=0:
		check,k=help_check_diagonal(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		j-=1
		i-=1
	i,j=replace[king[0]],int(king[1])
	while j<=8 and i>=0:
		check,k=help_check_diagonal(i,j,s1,s2)
		if k==1:
			break			
		elif k==2:
			return check
		j+=1
		i-=1
	i,j=replace[king[0]],int(king[1])
	while j>=1 and i<=7:
		check,k=help_check_diagonal(i,j,s1,s2)
		if k==1:
			break
		elif k==2:
			return check
		j-=1
		i+=1
	i,j=replace[king[0]],int(king[1])
	return help_check_knight(i,j,s1) or help_check_knight(i,j,s1)

def help_check_knight(i,j,s1):
	if s1=="W"and (board[str(1+j)[i-1]][:2] or board[str(1+j)[i+1]][:2])==s1+"P":
		return True
	elif s1=="B" and (board[str(1-j)[i-1]][:2] or board[str(1-j)[i+1]][:2])==s1+"P":
		return True
	return False

def help_check_diagonal(i,j,s1,s2):
	if board[str(j)][i][0]==s2:
		return False,1
	if (board[str(j)][i][:2]==(s1+"Q" or s1+"B")):
		return True,2
	return False,0
	
def help_check_inline(i,j,s1,s2):
	if board[str(j)][i][0]==s2:
		return False,1
	if (board[str(j)][i][:2]==(s1+"R" or s1+"Q")):
		return True,2
	return False,0
	
def help_check_knight(i,j,s1):
	l=[[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[1,-2],[-2,1],[2,-1]]
	for x,y in l:
		if ((i+x) >=0 and (j+y) >0) and (board[str(i+x)][i+y]==s1+"N"):
			return True 
	return False
	
def can_move_inline(move):
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

def can_move_diagonal(move):
	i,i1=min(int(move[3]),int(move[5]))+1,min(replace[move[2]],replace[move[4]])+1
	j,j1=max(int(move[3]),int(move[5])),max(replace[move[2]],replace[move[4]])
	while i<j:
		if board[str(i)][i1][0] != ' ':
			return False
		i+=1
		i1+=1
	return True

def change_position(move):
	board[move[5]][replace[move[4]]]=board[move[3]][replace[move[2]]]
	board[move[3]][replace[move[2]]]="   │"

def unchange_position(move):
	board[move[3]][replace[move[2]]]="   │"
	board[move[5]][replace[move[4]]]=board[move[3]][replace[move[2]]]
	
def invalid_function_call():
	print("invalid move ,try again")

def diagonal_move(move,s2):
	return (abs(replace[move[2]]-replace[move[4]]) == abs(int(move[3])-int(move[5])))>0 and (board[move[5]][replace[move[4]]][0] in (s2,' ') and (can_move_diagonal(move)) )

def inline_move(move,s2):
	return (((move[2] == move[4]) or (move[3] == move[5])) and (board[move[5]][replace[move[4]]][0] in(" ",s2)) and (can_move_inline(move)))

def pawn_move(move,s1,s2):
	if (move[:4] in l1):
		del l1[move[:4]]
	d=((s2+"P"+move[4]+move[3]) if s1=="W" else (s1=="W" and s2+"P"+move[4]+move[4]))
	if (move[:2]==s1+"P") and 	((s1=="W" and ((int(move[3])>int(move[5])))) or (s1=="B" and (int(move[3])<int (move[5])))):	
		if ((move[2] is move[4]) and (abs(int(move[3])-int(move[5]))==1)and (board[move[5]][replace[move[4]]][0] in (' '))) \
		or (abs(replace[move[2]]-replace[move[4]])==1 and ((board[move[5]][replace[move[4]]][0]==s2))):
			change_position(move)
			return True
		elif (abs(replace[move[2]]-replace[move[4]])==1 and (board[move[5]][replace[move[4]]][0]==' ')) \
		and (board[move[3]][replace[move[4]]][0]==s2 and (s1=="W" and (d in l1))):
			change_position(move)
			board[move[3]][replace[move[4]]]='   │'
			del l1[d]
			return True		
		elif (move[2] is move[4]) and (abs(int(move[3])-int(move[5]))==2) and ((s1=="W" and move[3]=="7" )or (s1=="B" and move[3]=="2") and inline_move(move,s2)) :
			change_position(move)
			l1.setdefault(move[:2]+move[4:],1)
			return True
	invalid_function_call()
	return False
	
def check_promotion(move,s1):
	if (s1 == "W" and move[-1]=='1'):
		promotion("w",move[-2:])
	elif (s1 == "B" and move[-1]=='8'):
		promotion("b",move[-2:])
		
def king_move(move,s1,s2):			
	if move[:2]==s1+"K" and (abs(replace[move[2]]-replace[move[4]]) or abs(int(move[3])-int(move[5]))==1) and (board[move[5]][replace[move[4]]][0]in (s2,' ')):
		change_position(move)
		return True
	invalid_function_call()
	return False
	
def rook_move(move,s1,s2):
	if (move[:2]==s1+"R") and inline_move(move,s2):
		change_position(move)
		return True
	invalid_function_call()
	return False

def bishop_move(move,s1,s2):
	if (move[:2]==s1+"B") and diagonal_move(move,s2):
		change_position(move)
		return True
	invalid_function_call()
	return False

def queen_move(move,s1,s2):
	if(move[:2]==s1+"Q") and (diagonal_move(move,s2) or inline_move(move,s2)):
		change_position(move)
		return True
	invalid_function_call()
	return False

def knight_move(move,s1,s2):
	if (move[:2]==s1+"N") and ((abs(replace[move[2]]-replace[move[4]]),abs(int(move[3])-int(move[5])))is (1,2) or (2,1)) and (board[move[5]][replace[move[4]]][0]in (s2,' ')):
		change_position(move)
		return True
	invalid_function_call()
	return False

def promotion(promote,at):
	new=input("['R' for Rook, 'N' for Knight, 'B' for Bishop, 'Q' for Queen]").upper()
	if new not in ('R','N','Q','B'):
		print("enter valid piece")
	elif promote == 'b':
		board[at[1]][replace[at[0]]]="B"+new+" │"
	else:
		board[at[1]][replace[at[0]]]="W"+new+" │"
		
def update_castling_check(position,check=' '):
	l.append(position)
	return check not in l

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

def check_for_checkmate(king,s1,s2):
	i,j=replace[king[0]],int(king[1])
	lp=[[1,0],[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[0,1],[-1,0]]
	for x,y in l:
		if ((i+x)>=0 and (j+y)>0) and board[str(j+y)[i]][0] not in (s2,' ') and check_for_check(king,s1,s2):
			return True
	return False

def Game_Start():
	check,k=False,0
	king_position=['E1','E8']
	castle_White_left,castle_White_right="WKE8H8","WKE8A8"
	castle_Black_left,castle_Black_right="BKE1H1","BKE1A1"
	castling_black=castling_white=True
	while True:
		(s1,s2)=(("W","B") if k%2==0 else ("B","W"))
		check=check_for_check(king_position[k%2],s1,s2)
		if castling_white and (turn[k%2]==0):
			print(r"For Castling input format: wke8(h8,a8) or bke1(h1,a1) ")
		elif castling_black and turn[k%2]:
			print(r"For Castling input format: wke8(h8,a8) or bke1(h1,a1) ")
		next_move=True
		print(turn[k%2]+"'s turn")
		entered_move=input().upper()
		piece=entered_move[1]
		if entered_move[0] is not s1:
			continue
		if len(entered_move)!=6 or ((entered_move[2] or entered_move[4])not in replace.keys()) \
		or(int((entered_move[3]) or int(entered_move[5]))not in range(1,9)) :
			print("out of bound input")
			continue			
		elif (entered_move[:2] != board[entered_move[3]][replace[entered_move[2]]][:2]):
			print(r"Error: No Pawn Here,invalid input")
			continue
		elif (entered_move in (castle_White_left,castle_White_right))\
		and can_move_inline(entered_move) and update_castling_check('$',check=board[entered_move[-1]][replace[entered_move[-2]]][:2]):
			if castling_white:
				castle_move((replace[entered_move[2]]-replace[entered_move[4]])//2,'8')
		elif (entered_move in (castle_Black_left,castle_Black_right))\
		and can_move_inline(entered_move) and update_castling_check('$',check=board[entered_move[-1]][replace[entered_move[-2]]][:2]):
			if castling_black:
				castle_move((replace[entered_move[2]]-replace[entered_move[4]])//2,'1')	
		elif piece is "P": 
			next_move=pawn_move(entered_move,s1,s2)
			if next_move==False:
				continue	
		elif piece is "K":
			next_move=king_move(entered_move,s1,s2)
			if next_move==False:
				continue
			king_position[k%2]=entered_move[-2:]
			if k%2==0:
				castling_white=False
			else:
				castling_black=False
		elif piece is "R":
			next_move=rook_move(entered_move,s1,s2)
			if next_move==False:
				continue
			update_castling_check(entered_move[:2],check=' ')	
		elif piece is "B":
			next_move=bishop_move(entered_move,s1,s2)
			if next_move==False:
				continue	
		elif piece is "Q":
			next_move=queen_move(entered_move,s1,s2)
			if next_move==False:
				continue	
		elif piece is "N":
			next_move=knight_move(entered_move,s1,s2)
			if next_move==False:
				continue
		check=check_for_check(king_position[k%2],s1,s2)
		if check==True:
			if check_for_checkmate(king_position[k%2],s1,s2):
				print("GAME OVER",center(42,'*'))
				print(turn[k%2]+ " wins")
				break
			print("CHECKED King!")
			unchange_position(entered_move)
			continue
		k+=1
		printboard()
	print("Number of turns to victory: %s"%(k//2))
	
Game_Start()
