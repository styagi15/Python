#!/usr/bin/python
#import Bio

   

def findLCS(read, cassette, rIndex, cIndex,cassettes):
  
  LCS=''
  while True:
    if read[rIndex] == cassette[cIndex]:
      LCS+= read[rIndex]
      rIndex= rIndex +1
      cIndex= cIndex +1
    #elif checkLCS(cIndex,cassettes)==True:
    else:
      break

  #print(LCS)
  
  return LCS

def findMaxLCS(read, cassettes, rIndex, cIndex):
  #print(read)
  maxLCS=''
  #print(len(cassettes))
  for i in range (0,len(cassettes)):
    LCS=findLCS(read, cassettes[i],rIndex, cIndex,cassettes)
     
    if len(LCS) > len(maxLCS):
      
      maxLCS=LCS
       
      
 
  rIndex= rIndex+len(maxLCS)
  cIndex= cIndex+len(maxLCS)
  return maxLCS ,rIndex ,cIndex

def findConsensus(cassettes, cIndex):
  #print (cassettes)
  con=[]
  for i in range(0,len(cassettes[1])-26):
    holder=[]
    for j in range(0,len(cassettes)):
      holder.append(cassettes[j][i])
    con.append(holder)
  con2=[]
  for k in range (0,len(con)):
    if con[k].count('G')==16 or (con[k].count('G')==14) :
      con2.append('g')
    elif con[k].count('A')==16 or (con[k].count('A')==14): #con[k][1]=='-'
      con2.append('a')
    elif con[k].count('C')==16 or (con[k].count('C')==14):
      con2.append('c')
    elif con[k].count('T')==16 or (con[k].count('T')==14):
      con2.append('t')
    elif con[k].count('-')>=10:
      con2.append('-')
    else:
      con2.append('n')
  #print(con)      
  #print(con2)

  return con2[cIndex]

def checkGap(LCS, cassettes, cIndex):
  
  #print(rIndex)
  #print(cIndex)

  #nuc= findConsensus(cassettes, cIndex)
  #LCS=LCS+ str(nuc)
  #cIndex=cIndex+1
    
  if findConsensus(cassettes, cIndex)== '-':
    LCS=LCS+'-'
    cIndex=cIndex+1
    return LCS, cIndex
  else:
    return LCS, cIndex
    #print(rIndex)
  #elif findConsens
  
  
  #elif (findConsensus(cassettes, cIndex)).isalpha():
    
    
   

def deletenuc(read, cassettes, rIndex, cIndex):

  if len(findMaxLCS(read, cassettes, rIndex+1, cIndex))>=3:
  
    return True
  else:
    return False
    
def insertnuc(LCS, read, cassettes, rIndex, cIndex):

  if len(findMaxLCS(read, cassettes, rIndex, cIndex+1))>=3:
    return True
  else:
    return False

#def subsnuc(
  

#def checkgaps(


def align(read, cassettes):
  #print(read)
  #print('hi')
  #print(cassettes)
  rIndex=0
  cIndex=0
  alignedRead=''
  LCS=''
  delrec=[]
  insertrec=[]
  substrec=[]
  
  #print(read)
  while rIndex<= len(read):
    #print(read)
    
    #print(len(read))
    #print(rIndex)
    LCS, rIndex, cIndex= findMaxLCS(read, cassettes,rIndex, cIndex)
    #print(rIndex)
    #print(cIndex)
    #print(LCS)
    LCS, cIndex= checkGap(LCS, cassettes,cIndex)
    
    #print(rIndex,cIndex)
    #print(LCS)      
    
    #if deletenuc(read, cassettes, rIndex,cIndex)==True:
      #delrec.append(rIndex)
      #rIndex= rIndex+1
    if len(LCS)<=6 :
      #print (LCS, rIndex)
      #print('enter')
      if insertnuc(LCS, read, cassettes, rIndex, cIndex)==True:
        #print(True, LCS)
        insertrec.append(rIndex)
        nuc= findConsensus(cassettes, cIndex)
        cIndex=cIndex+1
        LCS= LCS+nuc
      else:
        LCS, cIndex= checkGap(LCS, cassettes,cIndex)
    
    #elif subsnuc(LCS, read, cassettes, rIndex, cIndex)==True:
      

    
    #else:
 #     LCS, cIndex= checkLCS(LCS, cassettes,cIndex)

    
  

    
    #  nuc= findConsensus(cassettes, cIndex)
    #  LCS= LCS+nuc
    #   cIndex=cIndex+1
    #      rIndex=rIndex+1
    
    alignedRead= alignedRead+ str(LCS)
    print(alignedRead)
  
  return alignedRead

def main():
  FASTA=input('Enter FASTA file:')
  reference=input('Enter reference file:')
  in_file=open(FASTA, 'r')
  in_file1=open(reference,'r')


  line_list=[] 
  line_list1=[]



  for line in in_file:
    line=line.strip()
    line_list.append(line)
  readnames=line_list[::2]        #list of the read headers
  reads=line_list[1::2]         #list of sequences only

  for line1 in in_file1:
    line1=line1.strip()
    line_list1.append(line1) 
  cassettes=line_list1[1::2]
  refnames=line_list1[::2]

  #for i in cassettes:
  #  print(len(i))
  #print(cassettes)
  #print(reads)
  A=[]
  for i in reads:
    #print(i[0])
    alignedRead=align(i,cassettes)
    A.append(alignedRead)
    #print(align(i,cassettes))
    #out = open("out.txt", "w")
    #out.write(align(i, cassettes)
    #out.close()
 
  #print(A)
  #con=findConsensus(0,cassettes)
  #print(con)
