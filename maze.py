import pygame
from random import *
from collections import defaultdict

pygame.init()

blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,255,0)
yellow=(255,255,0)

SCREEN=pygame.display.set_mode((600,600))
pygame.display.set_caption('maze')
clock=pygame.time.Clock()
crashed=False
pygame.display.update()   
SCREEN.fill(blue)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    clock.tick(60)

pygame.quit
quit()    

for row in range(0,600,20):
    
    for col in range(0,600,20):
                    
            pygame.draw.line(SCREEN,yellow,(row,col),(row,col+20))
for col in range(0,620,20):
    for row in range(0,600,20):
            pygame.draw.line(SCREEN,yellow,(row,col),(row+20,col))

pygame.draw.rect(SCREEN,green,(0,0,20,20))           
pygame.draw.rect(SCREEN,red,(580,580,20,20))
pygame.display.update()

class grid:
    def __init__(self,xcod,ycod,cid):
        self.xcod=xcod
        self.ycod=ycod
        self.cid=cid
        self.graphi=set()
    def graphy(self,g):
        self.graphi.add(g)
count=0
xcod=10
ycod=10
glist=[]

for i in range(0,30):
    xcod=10
    for j in range(0,30):
        
        count=count+1
        cid=count
        glist.append(grid(xcod,ycod,cid))
        xcod=xcod+20
    ycod=ycod+20

status=[]
status.append(1)
visited=[]
visited.append(0)
upper=[]
left=[]
right=[]
lower=[]
rg=29
lg=30
for i in range(1,30):
    right.append(rg)
    left.append(lg)
    rg=rg+30
    lg=lg+30

for i in range(0,29):
    upper.append(i)
    lower.append(i+871)
    
c=1

for i in range(1,900):
    status.append(0)
 
while(c!=900):
    x=choice(visited)
    f=0
    n=[]
    
    
    for i in range(0,29):
    
        if(x==upper[i]):#top row
            f=1
            if(x==0):
                l=2
                n.append(x+1)
                n.append(x+30)
            else:
                l=3
                n.append(x+1)
                n.append(x+30)
                n.append(x-1)
        if(x==left[i]):#left column
            f=1
            if(x==870):
                l=2
                n.append(x+1)
                n.append(x-30)
            else:
                l=3
                n.append(x+1)
                n.append(x+30)
                n.append(x-30)
        if(x==right[i]):#right column
            f=1
            if(x==29):
                l=2
                n.append(x-1)
                n.append(x+30)
            else:
                l=3
                n.append(x-1)
                n.append(x+30)
                n.append(x-30)
        if(x==lower[i]):#bottom row
            f=1
            if(x==899):
                l=2
                n.append(x-1)
                n.append(x-30)
            else:
                l=3
                n.append(x-1)
                n.append(x+1)
                n.append(x-30)
    if(f==0):
        f=1
        l=4
        n.append(x-1)
        n.append(x+1)
        n.append(x-30)
        n.append(x+30)
        
      
    suc=1   
    while(suc!=0 and l>0 ): 
        y=choice(n)
        
        n.remove(y)
        l=l-1
        
        
        if(status[y]==0):
            suc=0
                
            if(y==x+1):#right neighbour
                f=0
                pygame.draw.line(SCREEN,blue,(glist[x].xcod+10,glist[x].ycod-10),(glist[x].xcod+10,glist[x].ycod+10))
                visited.append(y)
                glist[x].graphy(y)
                status.pop(y)
                status.insert(y,1)
                c=c+1
                
                
            if(y==x+30):#below neighbour
                f=0
                pygame.draw.line(SCREEN,blue,(glist[x].xcod-10,glist[x].ycod+10),(glist[x].xcod+10,glist[x].ycod+10))
                visited.append(y)
                glist[x].graphy(y)
                status.pop(y)
                status.insert(y,1)
                c=c+1
                
                
            if(y==x-30):#above neighbour
                f=0
                pygame.draw.line(SCREEN,blue,(glist[x].xcod-10,glist[x].ycod-10),(glist[x].xcod+10,glist[x].ycod-10))
                visited.append(y)
                glist[x].graphy(y)
                status.pop(y)
                status.insert(y,1)
                c=c+1
                
                
            if(y==x-1):#left neighbour
                f=0
                pygame.draw.line(SCREEN,blue,(glist[x].xcod-10,glist[x].ycod-10),(glist[x].xcod-10,glist[x].ycod+10))
                visited.append(y)
                glist[x].graphy(y)
                status.pop(y)
                status.insert(y,1)
                c=c+1
pygame.display.update()
graph=defaultdict(list)            
for i in range(0,900):
    graph[i]=glist[i].graphi
    #print(graph[i])
    
dfs.dfs(graph,0)
p=dfs.shortest_path(graph,0,899)
        
pygame.display.update()
pt=0

while(p[pt]!=899):
    m=p[pt]
    n=p[pt+1]
    pygame.draw.line(SCREEN,red,(glist[m].xcod,glist[m].ycod),(glist[n].xcod,glist[n].ycod),3)
    clock.tick(13)
    pygame.display.update()
    pt=pt+1
                

def dfs(graph, start):#1
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

    

def dfs_paths(graph, start, goal):#1
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                
                

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None

