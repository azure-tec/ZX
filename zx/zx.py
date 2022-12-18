import os
from time import sleep
import array
import random

fname = input("filename: ")
f = open(fname)
lines = f.read().splitlines()
f.close()

print("loading '" + fname + "'")
x = "0"
a = 0
b = 0
c = 0
m = 0
m2 = 0
mans = 0

nvars = {'null':'null'}

for x in lines:
    ans = x.split("|")
    if ans[0] == "pt":
      if ans[1] == "v>a":
        print(a)
      elif ans[1] == "v>b":
        print(b)
      elif ans[1] == "v>c":
        print(c)
      else:
        print(ans[1])
    
    if ans[0] == "it":
      if ans[1] == "a":
        a = input(ans[2])

      if ans[1] == "b":
        b = input(ans[2])

      if ans[1] == "c":
        c = input(ans[2])
    
    if ans[0] == "vt":
      if ans[1] == "a":
        a = ans[2]

      if ans[1] == "b":
        b = ans[2]
  
      if ans[1] == "c":
        c = ans[2]

    if ans[0] == "ct":
      os.system("clear")

    if ans[0] == "wt":
      sleep(int(ans[1]))
      
      if ans[2] == "pt":
         if ans[1] == "v>a":
            print(a)
         elif ans[1] == "v>b":
            print(b)
         elif ans[1] == "v>c":
            print(c)
         else:
            print(ans[1])
      
      if ans[2] == "ct":
        os.system("clear")

    if ans[0] == "jt":
       if ans[3] == "a":
        a = ans[1] + ans[2]

       if ans[3] == "b":
        b = ans[1] + ans[2]
  
       if ans[3] == "c":
        c = ans[1] + ans[2]

    if ans[0] == "tama#tama":
       print("MEOW")

    if ans[0] == "m+":
       if ans[3] == "a":
        a = int(ans[1])+int(ans[2])

       if ans[3] == "b":
        b = int(ans[1])+int(ans[2])
  
       if ans[3] == "c":
        c = int(ans[1])+int(ans[2])

    if ans[0] == "m-":
       if ans[3] == "a":
        a = int(ans[1])-int(ans[2])

       if ans[3] == "b":
        b = int(ans[1])-int(ans[2])
  
       if ans[3] == "c":
        c = int(ans[1])-int(ans[2])

    if ans[0] == "m*":
       if ans[3] == "a":
        a = int(ans[1])*int(ans[2])

       if ans[3] == "b":
        b = int(ans[1])*int(ans[2])
  
       if ans[3] == "c":
        c = int(ans[1])*int(ans[2])

    if ans[0] == "m/":
       if ans[3] == "a":
        a = int(ans[1])/int(ans[2])

       if ans[3] == "b":
        b = int(ans[1])/int(ans[2])
  
       if ans[3] == "c":
        c = int(ans[1])/int(ans[2])

    if ans[0] == "rn":
       if ans[2] == "a":
        a = random.randrange(int(ans[1]))

       if ans[2] == "b":
        b = random.randrange(int(ans[1]))
  
       if ans[2] == "c":
        c = random.randrange(int(ans[1]))
