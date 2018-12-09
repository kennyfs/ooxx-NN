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
can=[]
n=0
color=1
b=0
w=0
def dump():
	a='  0 1 2\n'
	for x in range(3):
		a+=str(x)
		for y in range(3):
			if book[x][y]==0:
				a=a+textcolor.color+'172'+textcolor.end+textcolor.bg+'172'+textcolor.end+u'\u25cf '+textcolor.reset
			elif book[x][y]==1:
				a=a+textcolor.color+'16'+textcolor.end+textcolor.bg+'172'+textcolor.end+u'\u25cf '+textcolor.reset
			else:
				a=a+textcolor.color+'255'+textcolor.end+textcolor.bg+'172'+textcolor.end+u'\u25cf '+textcolor.reset
		a=a+'\n'
	print (u'{}'.format(a))
for i in range(1000000):
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
	if win()==1:
		b+=1
	if win()==2:
		w+=1
print 'black='+str(b)+'/1000000\nwhite='+str(w)+'/1000000\nb+w='+str(b+w)
