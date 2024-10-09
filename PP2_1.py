'''
Lesson: If Statements
Author: Alex Liang
Date Created: October 9th, 2024
Date Last Modified: October 9th, 2024
'''

def q1(): 
  #Write Assignment code here

  num = int(input("Input a number: "))
  if num % 2 == 1:
    print(f'{num} is odd')
  if num % 2 == 0: 
    print(f'{num} is even')

def q2(): 
  #Write Assignment code here
  student = "student"
  teacher = "teacher"
  name = str(input("Input a name: "))
  if name != "Kalisz":
    print(student)
  if name == "Kalisz":
    print(teacher)


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
