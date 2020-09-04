# Author: Jiarou Deng dpj5243@psu.edu
C=0
GPA=0 
for n in range(1,4):
 g= input(f"Enter your course {n} letter grade: ")
 c= input(f"Enter your course {n} credit: ")
 if g == "A":
   p = 4.0
 elif g == "A-":
   p = 3.67
 elif g == "B+":
   p = 3.33
 elif g == "B":
   p = 3.0
 elif g == "B-":
   p = 2.67
 elif g == "C+":
   p = 2.33
 elif g == "C":
   p = 2.0
 elif g == "D":
   p = 1.0
 else:
   p = 0.0
 print(f"Grade point for course {n} is: {p}")
 GPA= GPA + p*float(c)
 C= C+float(c)
GPA1 = GPA/C
print(f"Your GPA is:{GPA1}")