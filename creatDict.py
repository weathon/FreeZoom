import pickle
f=open("dict.dict","r")
string=f.read()
f.close()
mydict=[]
block=string.split("\n\n")
print(block)
for b in block:
    key=str(b[:2])+str(b[3:5])
    # print(key,end="\n")
    myIndex=int(key,2)#转化为十进制储存
    value=b[5:].replace("\n","")
    print(value)
    