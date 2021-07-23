import sys
from math import log,trunc
import os
def numberlistS(nums, limit):
    prefix = []
    valparr=[]
    sum = 0
    index=0
    for num in nums[::-1]:
        index=index+1
        sum += num
        prefix.append(num)
        if limit-num>2:
            prefix.append(num)
            valparr.append(limit-num)
        if (limit-num) ==2:
            valparr.append(prefix[index-1])
        if (limit-num) ==1:
            valparr.append(nums[::-1][index-2])   
        if (limit-num) ==0:
            valparr.append(prefix[index-1])
        return valparr
        return valparr
def pNEAAS(nbr1):
    nbr=nbr1
    print("")
    NEAAS(nbr1)        
def pNEAAC(nbr1):
    nbr=nbr1
    print("")
    NEAAC(nbr1)
def NEAAS (nbr):
    Pval=[]
    if (nbr==1):
         
         Pval.append(1)
         if "-" in str(x):
               print ('-'+str(Pval[0])+"-")
         else:
               print (str(Pval[0])+"+")
    NEA=1
    if "-" in str(nbr):
           f=int(str(nbr).replace('-',''))
           f=int(f)
    else:
           f=nbr
           f=int(f)
    NEAarr=[]
    
    for i in range  (2,f):
        if NEA % i != 0 :
           NEA= NEA * (i ** trunc (log(f,i)))
           NEAarr.append(i)
    if nbr == 2:
        print(2)
    if nbr ==-2:
        print (-2)
    if nbr !=1 and nbr !=2 and nbr !=-2:
        valok=0
        for val in numberlistS(NEAarr,f):
            Pval.append(str(val))
            valok=valok+val
        if (f-valok)!=0:
            if f-valok in NEAarr:
                Pval.append(str(f-valok))
            if f-valok not in NEAarr:
                NEAAS(int(f-valok))
            if "-" in str(x):
                s = "-"
                s = s.join(Pval)
                Parrok=s.split("-")
            else:
                s = "+"
                s = s.join(Pval)
                Parrok=s.split("+")
            for  valpok in Parrok:
                if int(valpok) in NEAarr:
                    if "-" in str(x):
                         print (-int(valpok))
                    else:
                         print (int(valpok))
                else:
                    #print(valpok)
                    NEAAS(valpok)
def NEAAT (nbr):
    Pval=[]
    if (nbr==1):
         Pval.append(1)
         if "-" in str(nbr):
               print ('-'+str(Pval[0])+"-")
         else:
                print (str(Pval[0])+"+")
    NEA=1
    if "-" in str(nbr):
           f=int(str(nbr).replace('-',''))
    else:
           f=nbr
    NEAATrrs=[]
    NEAATrr=[]
    NEAATrrSolution=[]
    Solution=[]
    
    for i in range  (2,f):
        if NEA % i != 0 :
           NEA= NEA * (i ** trunc (log(f,i)))
           NEAATrr.append(i)


    if (nbr!=1):
        valok=0
        for val in numberlistC(NEAATrr,f):
            if (nbr-sum_of_list(Pval)-val)!=1:
                Pval.append(str(val))
                valok=valok+val

        reste=int(f-valok)
        if (f-valok)!=0:
            if f-valok in NEAATrr:
                 Pval.append(str(f-valok))
            if f-valok not in NEAATrr:
                NEAAT(int(f-valok))

            if "-" in str(nbr):
                s = "-"
                s = s.join(Pval)
                print ('-'+str(s))
            else:
                s = "+"
                s = s.join(Pval)
                print (s)
				
				
				
    fok=int(nbr)+1
    for i in range  (2,fok):
        if NEA % i != 0 :
            Solution.append(i)
            print("PRIME    :"+str(i))
            print()
def NEAATP (nbr):
    Pval=[]
    if (nbr==1):
         Pval.append(1)
         if "-" in str(x):
               print ('-'+str(Pval[0])+"-")
         else:
               print (str(Pval[0])+"+")
    NEA=1
    if "-" in str(nbr):
           f=int(str(nbr).replace('-',''))
    else:
           f=nbr
   
    NEAATrr=[]
    
    for i in range  (2,f):
        if NEA % i != 0 :
           NEA= NEA * (i ** trunc (log(f,i)))
           NEAATrr.append(i)
    if (nbr!=1):
        valok=0
        for val in numberlistC(NEAATrr,f):
            Pval.append(str(val))
            valok=valok+val
        if (f-valok)!=0:
            if f-valok in NEAATrr:
                Pval.append(str(f-valok))
            if f-valok not in NEAATrr:
                NEAAT(int(f-valok))
            if "-" in str(x):
                s = "-"
                s = s.join(Pval)
                print ('-'+str(s))
            else:
                s = "+"
                s = s.join(Pval)
                print (s)
def PRGG(nbr):
    
    Parr=[]
    NEA=1
    nbrok=int(nbr)+2
    for i in range  (2,nbr):
        if NEA % i != 0 :
            NEA= NEA * (i ** trunc (log(nbr,i)))
            Parr.append(i)
    for indexx in range (0,len(Parr)-1):
            if (nbr-Parr[indexx]) in Parr:
                    if (nbr)%2!=0:
                        print("Goldbach IMPAir number")
                        print (str(nbr)+"="+str(nbr-Parr[indexx])+"+"+str(Parr[indexx]))
                    else:
                         print (str(nbr)+"="+str(nbr-Parr[indexx])+"+"+str(Parr[indexx]))                     
def numberlist(nums, limit):
    prefix = []
    sum = 0
    for num in nums:
        sum += num
        prefix.append(num)
        if sum > limit:
            del prefix[-1]
            return prefix
def NEAA (nbr):
    Pval=[]
    #print (nbr)
    # if (nbr==1):
         # Pval.append(1)
         # if "-" in str(x):
               # print ('-'+str(Pval[0])+"-")
         # else:
               # print (str(Pval[0])+"+")
    NEA=1
    if "-" in str(nbr):
           f=int(str(nbr).replace('-',''))
    else:
           f=nbr
   
    NEAarr=[]
    
    for i in range  (2,f):
        if NEA % i != 0 :
           NEA= NEA * (i ** trunc (log(f,i)))
           NEAarr.append(i)
    if (nbr!=1):
        valok=0
        for val in numberlist(NEAarr,f):
            Pval.append(str(val))
            valok=valok+val
        if (f-valok)!=0:
            if f-valok in NEAarr:
                Pval.append(str(f-valok))
            if f-valok not in NEAarr:
                NEAA(int(f-valok))
            if "-" in str(x):
                s = "-"
                s = s.join(Pval)
                print ('-'+str(s))
            else:
                s = "+"
                s = s.join(Pval)
                print (s)
def timeout():
    print("")
    print("")
    #print("Try IT !!!")
def pNEAA(nbr1):
    nbr=nbr1
    print("")
    NEAA(nbr1)
def numberlistC(nums, limit):
    prefix = []
    sum = 0
    for num in nums:
        sum += num
        prefix.append(num)
        if sum > limit:
            del prefix[-1]
            return prefix
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + int(val)
  return total
print()
print()
print("this program use PYTHON 3")
print()
print()
print("this program has been realized by ")
print()
print("                                                   ALAMATA SOD")
print()
print()
print (">>This program can decompose any  integer [+,-]  into a  prime addition term (termisation)")
print()
print("IF so")
print ("          - Most Simple  Termisation  [S]")
print()
print("          - Termisation  [T]")
print()
print()
print(">>This program can  also find  all GOLDBACH number [pair,impair] until the specified one [G]") 
print()
print()
stop=0
while stop==0:
	print()
	print()
	q1=input("Do  you want make Most Simple TERMISATION  [S], TERMISATION [T] or  find  all   GODLBACH NUMBER until the specified one  [G]  or [X] to EXIT.?")
	q1=str(q1)
	print()
	print()
	if q1=="T":
			print()
			print()
			x=input ("Enter  the Integer  you desire  to decompose  into  Prime Addition  Term  : ")
			x=int(x)
			pNEAA(x)
	if q1=="S":
			print()
			print()
			x=input ("Enter  the Interger  you desire  to decompose  into Most  Simple Prime Addition  Term   : ")
			x=int(x)
			print()
			print()
			nbr=x
			print("")
			print("") 
			pNEAAS(nbr)

	if q1=="G":

			x=input ("Enter  any integer  as base  to find   all  GOLDBACH number  until the specified one: ")
			x=int(x)
			print()
			print()
			for k in  range  (1,x+1):
					print()
					PRGG(k)
	if q1=="X":
		stop=1