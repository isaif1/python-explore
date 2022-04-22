from operator import is_


def sayHi(name,age): # paramter will be recieve here
    print('hello '+ name+ "your age is"+str(age))

sayHi('saif',23)#arguments will be pass from here

def cube(num):
    return num*num*num

print(cube(3))

is_male = True
is_tall = False

if is_male or is_tall:
    print("you are male or tall or both")
else:
    print("you are neither male or tall")

if is_male or not is_tall:
    print("you are either male or sort")