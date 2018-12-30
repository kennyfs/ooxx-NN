from random import randrange
class textcolor:
	bg   ="\x1b[48;5;"
	color="\x1b[38;5;"
	end  ="m"
	reset="\x1b[0m"
book=[[0,0,0],[0,0,0],[0,0,0]]
def win():
	if(book[0][0]==1 and book[0][1]==1 and book[0][2]==1):
		return 1
	if(book[1][0]==1 and book[1][1]==1 and book[1][2]==1):
		return 1
	if(book[2][0]==1 and book[2][1]==1 and book[2][2]==1):
		return 1
	if(book[0][0]==1 and book[1][0]==1 and book[2][0]==1):
		return 1
	if(book[0][1]==1 and book[1][1]==1 and book[2][1]==1):
		return 1
	if(book[0][2]==1 and book[1][2]==1 and book[2][2]==1):
		return 1
	if(book[0][0]==1 and book[1][1]==1 and book[2][2]==1):
		return 1
	if(book[0][2]==1 and book[1][1]==1 and book[2][0]==1):
		return 1
		#black end
	if(book[0][0]==2 and book[0][1]==2 and book[0][2]==2):
		return 2
	if(book[1][0]==2 and book[1][1]==2 and book[1][2]==2):
		return 2
	if(book[2][0]==2 and book[2][1]==2 and book[2][2]==2):
		return 2
	if(book[0][0]==2 and book[1][0]==2 and book[2][0]==2):
		return 2
	if(book[0][1]==2 and book[1][1]==2 and book[2][1]==2):
		return 2
	if(book[0][2]==2 and book[1][2]==2 and book[2][2]==2):
		return 2
	if(book[0][0]==2 and book[1][1]==2 and book[2][2]==2):
		return 2
	if(book[0][2]==2 and book[1][1]==2 and book[2][0]==2):
		return 2
	for i in range(3):
		for j in range(3):
			if(book[i][j]==0):
				return -1
	return 0
def init():
	for i in range(3):
		for j in range(3):
			book[i][j]=0
f=open('ooxxdata.txt','a')
f.truncate(0)
can=[]
game=[]
color=1
def printonehot(color):
	white=[]
	black=[]
	for x in range (3):
		for y in range (3):
			if book[x][y]==1:
				white.append(0)
				black.append(1)
			if book[x][y]==2:
				white.append(1)
				black.append(0)
			if book[x][y]==0:
				white.append(0)
				black.append(0)
	if color==1:
		game.append([])
		for i in range(9):
			game[-1].append(black[i])
		for i in range(9):
			game[-1].append(white[i])
	if color==2:
		game.append([])
		for i in range(9):
			game[-1].append(white[i])
		for i in range(9):
			game[-1].append(black[i])
for i in range(100):
	init()
	color=1
	num=0
	game=[]
	while(win()==-1):
		can=[]
		for x in range(3):
			for y in range(3):
				if(book[x][y]==0):
					can.append([x,y])
		n=randrange(0,len(can))
		book[can[n][0]][can[n][1]]=color
		color=(not(color-1))+1
		printonehot(color)
		num+=1
	ww=win()
	if not ww==0:
		for j in range(num):
			if i%2+1==ww:
				game[j].append(1)
			else:
				game[j].append(-1)
	if win()==0:
		for j in range(num):
			game[j].append(0)
	for j in game:
		for k in j:
			f.write(str(k)+' ')
		f.write('\n')
f.close()
