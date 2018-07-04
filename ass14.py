#Q.1- Write a Python program to read last n lines of a file

n=int(input("ENTER THT VALUE HOW MUCH LINES U WANT TO PRINT "))
c=0
f=open('ass14.txt','r',encoding='utf8')
content=f.readlines()
print(content)
for i in content:
     c=c+1
     if(c>n):
       print(i)
f.close

#Q.2 Write a Python program to count the frequency of words in a file.


 with open("abc.txt",'r') as f:
     content = f.read()

 words = content.split()
 print(words)
 s = set(words)
 print(s)
 for n in s:
     print(n,words.count(n))


# Q.3- Write a Python program to copy the contents of a file to another file
 with open ('abc.txt','r') as f1:
     with open('cde.txt','w') as f2:
         for line in f1:
             f2.write(line)

# Q.4- Write a Python program to combine each line

 with open ('abc.txt','r') as f1:
      con1=f1.readlines()

 with open('cde.txt', 'r') as f2:
     con2 =f2.readlines()

 i = 0
 for n in con1:
     print(con1[i]+con2[i])
     i = i + 1
# Q.5- Write a Python program to write 10 random
# numbers into a file.
 import random
 with open ('abc.txt','w') as f1:
  for i in range(10):
   num=random.randint(1,9)
   f1.write(str(num))
   f1.write("\n")
 with open ('abc.txt','r') as f1:
     con=f1.readlines()
     con.sort()

 with open ('cde.txt','w') as f1:
  for i in con:
      f1.write(i)
      f1.write('\n')