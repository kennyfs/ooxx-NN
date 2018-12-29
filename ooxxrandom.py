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
n=0
color=1
b=0
w=0
def printonehot():
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
	for i in range(9):
		f.write(str(black[i])+' ')
	for i in range(9):
		f.write(str(white[i])+' ')
	f.write('\n')
for i in range(1):
	init()
	color=1
	while(win()==-1):
		can=[]
		for x in range(3):
			for y in range(3):
				if(book[x][y]==0):
					can.append([x,y])
		n=randrange(0,len(can))
		book[can[n][0]][can[n][1]]=color
		color=(not(color-1))+1
		printonehot()
	if win()==1:
		b+=1
		f.write("1\n")
	if win()==2:
		w+=1
		f.write("-1\n")
	if win()==0:
		f.write("0\n")

f.close()
