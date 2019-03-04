def minDistance(dist2,set,x):
	minimum=10000
	idx=0
	for i in range(x):
		if set[i]==0 and dist2[i]<=minimum:
			minimum=dist2[i]
			idx=i
	return idx

def dijkstra(matrix,s,d,n):
	r=[]
	for i in range(n):
		temp=[]
		temp.append(0)
		temp.append(0)
		r.append(temp)
	s-=1
	d-=1
	dist=[]
	setPermanent=[]
	print("1",dist)
	for i in range(n):
		dist.append(10000)
		setPermanent.append(0)
	dist[s]=0
	b=0
	print("2",dist)
	for i in range(n-1):
		a=minDistance(dist,setPermanent,n)
		setPermanent[a]=1
		r[a][1]=b
		b=a
		for j in range(n):
			print("3",dist)
			if setPermanent[j]==0 and matrix[a][j]>0 and dist[a]!=10000 and dist[a]+matrix[a][j]<dist[j]:
				dist[j]=dist[a]+matrix[a][j]
				print("4",dist)
		r[a][0]=dist[a]
	print("5",dist)
	return r

adjMatrix = [
	         [0,100,30,0,0],
	         [0,0,20,0,0],
	         [0,0,0,10,60],
	         [0,15,0,0,50],
	         [0,0,0,0,0]
	        ]
nodes=len(adjMatrix)
src=1
dst=2
route=dijkstra(adjMatrix,src,dst,nodes)
for i in route:
	print(i)
print("\nSource:", src)
print("\nDestination:", dst)
print("\nDistance:", route[dst-1][0])
print("\nRoutes: ", end='')
while(dst>src):
	print("(%d)" %dst, "-> ", end='')
	x=route[dst-1][0]
	y=route[dst-1][1]+1
	print("[%d" %x, end='')
	print(",%d" %y, end='')
	print("] -> ", end='')
	dst=y
print("(%d)" %src)