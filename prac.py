#!/usr/bin/python

L=['ABC','ABC']
con1=[]
for i in range (0,len(L[1])):
    #con.append(L[1][i])
  con=[]

  for j in range (0, len(L)):
    print(L[j][i])
    
    con.append(L[j][i])
  con1.append(con)

con2=[]
 
for k in range (0,len(con1)):
  if con1[k].count('A')==2:
    con2.append('a')
  elif con1[k].count('B')==2:
    con2.append('b')
  else:
    con2.append('n')
