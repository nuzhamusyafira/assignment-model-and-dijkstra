def isEqual(lenRow,lenCol):
    global table
    if lenRow<lenCol:
        temp=[]
        for x in range(lenCol):
            temp.append(0)
        for x in range(lenCol - lenRow):
            table.append(temp)
        lenRow=lenCol
    elif lenRow>lenCol:
        for x in range(lenRow):
            for y in range(lenRow - lenCol):
                table[x].append(0)
        lenCol=lenRow

def sortNumZero(arr):
    val=len(arr)-1
    temp=[]
    for a in arr:
        for i in range(len(a)):
            temp2=[]
            temp2.append(a[i])
            temp2.append(val)
            temp2.append(i)
            temp.append(temp2)
        val-=1
    temp.sort(key=lambda z: (-z[0], -z[1]))
    return temp

def countZero(x,y,table2):
    if y==1:
        table2=list(zip(*table2))
    temp=[]
    for i in range(x):
        temp.append(table2[i].count(0))
    return temp

def toZero(x,y,min):
    for i in range(x):
        for j in range(x):
            if y==1:
                table[j][i]=table[j][i]-min[i]
            else:
                table[i][j]=table[i][j]-min[i]

def minValue(x,y,table2):
    if y==1:
        table2=list(zip(*table2))
    temp=[]
    for i in range(x):
        temp.append(min(table2[i]))
    return temp

def crossZero(table2,sortZ,counter):
    row=[]
    col=[]
    for i in range(len(table2)):
        row.append(0)
        col.append(0)
    for i in sortZ:
        if i[1]==1:
            if table2[i[2]].count(0)>0:
                for j in range(len(table2[i[2]])):
                    if table2[i[2]][j]==0:
                        table2[i[2]][j]='#'
                counter+=1
                row[i[2]]=1
        else:
            temp=list(zip(*table2))
            if temp[i[2]].count(0)>0:
                for j in range(len(temp[i[2]])):
                    if table2[j][i[2]]==0:
                        table2[j][i[2]]='#'
                counter+=1
                col[i[2]]=1
    if counter<len(table2):
        temp2=[]
        for s in range(len(table2)):
            for x in range(len(table2)):
                if row[s]==0 and col[x]==0:
                    temp2.append(table2[s][x])
        newMin=min(temp2)
        for s in range(len(table2)):
            for x in range(len(table2)):
                if table2[s][x]=='#':
                    table2[s][x]=0
                if row[s]==0 and col[x]==0:
                    table2[s][x]-=newMin
                elif row[s]==1 and col[x]==1:
                    table2[s][x]+=newMin
        numZ=[]
        numZ.append(countZero(4,0,table2))
        numZ.append(countZero(4,1,table2))
        sortZ=sortNumZero(numZ)
        crossZero(table2,sortZ,0)
    else:
        for s in table2:
            for x in range(len(s)):
                if s[x]=='#':
                    s[x]=0

def costs(x,table2):
    flag=[]
    for i in range(x):
        flag.append(0)
    temp2=[]
    while sum(flag)<=x:
        c=[]
        for a in table2:
            c.append(a.count(0))
        if c.count(1)==0:
            break
        temp=[]
        idx=c.index(1)
        i=idx
        j=table2[idx].index(0)
        flag[j]=1
        for f in range(x):
            if table2[f][j]==0:
                table2[f][j]='*'
        c[idx]=0
        table2[i][j]='*'
        temp.append(i)
        temp.append(j)
        temp2.append(temp)
    for s in table2:
        for x in range(len(s)):
            if s[x]=='*':
                s[x]=0
    temp2=sorted(temp2)
    return temp2

table=[
       [5,7,9],
       [14,10,12],
       [15,13,16],
      ]
lenRow=len(table)
lenCol=len(table[0])
isEqual(lenRow,lenCol)
import copy
copyTable=copy.deepcopy(table)
minVal=minValue(lenRow,0,table)
toZero(lenRow,0,minVal)
minVal=minValue(lenCol,1,table)
toZero(lenCol,1,minVal)
numZero=[]
numZero.append(countZero(lenRow,0,table))
numZero.append(countZero(lenCol,1,table))
sortedZero=sortNumZero(numZero)
crossZero(table,sortedZero,0)                
result=costs(lenRow,table)
print("\nTabel mula-mula:")
for i in copyTable:
    print(i)
print("\nSetelah optimalisasi:")
for i in table:
    print(i)
print("\nHasil:")
res=0
for i in range(len(result)):
    res+=copyTable[result[i][0]][result[i][1]]
    if i==len(result)-1:
        print(copyTable[result[i][0]][result[i][1]],"=",res)
    else:
        print(copyTable[result[i][0]][result[i][1]],"+ ",end='')