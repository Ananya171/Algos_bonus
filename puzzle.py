
import sys
def puzzle_print(l1):  #prints the puzzle in human readable form
    i=0
    while(1):
        print(l1[i]," ",l1[i+1]," ",l1[i+2])
        i+=3
        if(i==9): break

def find_possiblemoves(l2):  # finds the possible moves 
    rownum=0
    direc=[]
    for i,v in enumerate(l2):
        if v=="_":
            if i<3: direc.append(2)
            elif i>2 and i<6: 
                direc.append(1)
                direc.append(2)
            else: direc.append(1)
            break
    if i%3==0: direc.append(4)
    elif i%3==2: direc.append(3)
    else:
        direc.append(3)
        direc.append(4)
    return direc,i

def move(l,command,p):    # generates a puzzle of a particular move choice
    l3=[]
    for i in l:
        l3.append(i)
    if command==2:
        l3[p]=l3[p+3]
        l3[p+3]="_"
    elif command==1:
        l3[p]=l3[p-3]
        l3[p-3]="_"
    elif command==3:
        l3[p]=l3[p-1]
        l3[p-1]="_"
    else: 
        l3[p]=l3[p+1]
        l3[p+1]="_"
    return l3

def find_hval(l4):      # finds the heuristic value of that puzzle from the goal
    coordinates={0:[1,1],1:[2,1],2:[3,1],3:[1,2],4:[2,2],5:[3,2],6:[1,3],7:[2,3],8:[3,3]}
    goal={"_":[1,1],"1":[2,1],"2":[3,1],"3":[1,2],"4":[2,2],"5":[3,2],"6":[1,3],"7":[2,3],"8":[3,3]}
    hval=0
    for ind,i in enumerate(l4):
        x1,y1=coordinates[ind]
        x2,y2=goal[i]
        val=abs(x1-x2)+abs(y1-y2)
        hval+=val
    return hval

def match(st):     # checks if goal is reached
    flag=0
    fin=["_","1","2","3","4","5","6","7","8"]
    for i in range(len(st)):
        if st[i]!=fin[i]:
            flag=1
            break
    return flag

st=[]
st1=[]
extract=sys.argv[1:]  #extracts the input from CLI
for x in extract:
    st.append(x)
for x in extract:
    st1.append(x)
ch=1                 #starts with the first heuristic value
while(ch<3):
    gval=0
    print("Using Heuristic ",ch,":")
    sort_array = []
    if ch==2:
        st=[]
        for x in st1:
            st.append(x)
    sort_array.append([st,[],find_hval(st)])
    mv = []
    puzzle_print(st)
    print("\n")
    while(match(st)!=0):
        gval+=1
        case,pos=find_possiblemoves(st)
        print("case:",case)
        temp_nxt=[]
        d={} 
        s={}
        for i in case:
            nxt_st=move(st,i,pos)
            total=0
            if "".join(nxt_st) not in s:
                if ch==1:
                    total=gval+find_hval(nxt_st)
                else: 
                    total=gval+0
                s["".join(nxt_st)]=total
            sort_array.append([nxt_st,mv+[i],find_hval(nxt_st)])
        sort_array.sort(key = lambda x: x[2])
        st = list(sort_array[0][0])
        mv = list(sort_array[0][1])
        del sort_array[0]
        
    if ch==1:
        for i in mv:
            c,pos=find_possiblemoves(extract)
            nxt=move(extract,i,pos)
            puzzle_print(nxt)
            print("\n")
            extract=nxt
    else:
        for i in mv:
            c,pos=find_possiblemoves(st1)
            nxt=move(st1,i,pos)
            puzzle_print(nxt)
            print("\n")
            st1=nxt
    ch+=1