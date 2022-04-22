employee_file=open('employee.txt','r')

print(employee_file.read())
print(employee_file.readline()) #it reads indivisual lines, but will read first line only
#have to read one more line by adding one more code into ot


print(employee_file.readlines()) #read all lines at once and put them in the list

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

#writting to file 
#in case of write it will remove previous data
employee_file=open('employee1.txt','w')

employee_file.write("\nToby - Human Resource")# writing something at the end, in new line

employee_file.close()



#appending to the file
employee_file=open('employee.txt','a')

employee_file.write("\nToby - Human Resource")# writing something at the end, in new line

employee_file.close()

#text ke alawa we can create html file as well

import random

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)
