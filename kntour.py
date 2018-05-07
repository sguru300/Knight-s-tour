class pix:
    def __init__(self):
        self.visited=0
        self.start=None
        self.end=None

class sample:
    def __init__(self):
        self.start=None
        self.end=None
        self.value=None
def adjacent(x,y,s):
    if(x+1<n):
        if(y+2<m and board[x+1][y+2].visited==0):
            s.append(board[x+1][y+2])
        if(y-2<m and board[x+1][y-2].visited==0):
            if(y-2>=0):
                
                s.append(board[x+1][y-2])
    if(x-1<n and x-1>=0):
        if(y+2<m and board[x-1][y+2].visited==0):
            s.append(board[x-1][y+2])
        if(y-2<m and board[x-1][y-2].visited==0):
            if(y-2>=0):
                s.append(board[x-1][y-2])
    if(x+2<n):
        if(y+1<m and board[x+2][y+1].visited==0):
            s.append(board[x+2][y+1])
        if(y-1<m and board[x+2][y-1].visited==0):
            if(y-1>=0):
                s.append(board[x+2][y-1])
    if(x-2<n and x-2>=0):
        if(y+1<m and board[x-2][y+1].visited==0):
            s.append(board[x-2][y+1])
        if(y-1<m and board[x-2][y-1].visited==0):
            if(y-1>=0):
                s.append(board[x-2][y-1])
    return len(s)

def findadjacent(x,y,s,count):
    board[x][y].visited=1
    count=count+1
    adjacent(x,y,s)
    #print(s)
    temp2=findnext(s)
    #print(count,"next coordinate to go is",temp2.start,temp2.end)
    if(temp2.start==None or temp2.end==None):
        print("Tour is not possible")
        return
    knight[temp2.start][temp2.end]=count
    s.clear()
    if(count<(n*m)):
        findadjacent(temp2.start,temp2.end,s,count)
def findnext(s):
    temp=sample()
    temp.value=9999
    t=[]
    #print("length",len(s))
    for i in range(len(s)):
        #print("adj len",adjacent(s[i].start,s[i].end,t))
        if(adjacent(s[i].start,s[i].end,t)<temp.value):
            #print("---",s[i].start,"---",s[i].end)
            t.clear()
            temp.value=adjacent(s[i].start,s[i].end,t)
            temp.start=s[i].start
            temp.end=s[i].end
        t.clear()
    return temp

        
        
n=int(input("Enter length of board : "))
m=int(input("Enter width of board : "))
if(n<=4 or m<=4):
    print("Tour is not possible")
    exit(1)
print("Enter coordinates of starting position : ")
x,y=map(int,input().split())
if(x>=n or y>=m):
    print("Invalid starting position")
    exit(1)

board=[None for i in range(n)]
knight=[None for i in range(n)]
for i in range(n):
    board[i]=[pix() for i in range(m)]
    knight[i]=[None for i in range(m)]
for i in range(n):
    for j in range(m):
        board[i][j].start=i
        board[i][j].end=j
k=0

s=[]
board[x][y].visited=1
knight[x][y]=1
findadjacent(x,y,s,1)
#print("s is now",s)


print("--------------------------")
for j in range(m):
    for k in range(n):
        print(knight[k][m-1-j],end="\t")
    print()
