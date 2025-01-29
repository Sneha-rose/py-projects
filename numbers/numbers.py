f=open('numbers.txt','r')
e=open("even.txt","w")
o=open('odd.txt','w')
n=f.read()
q=n.split()
for num in q:
    if int(num)%2 == 0:
        e.write(num+" ")
    else:
        o.write(num+" ")

f.close()
e.close()
o.close()
