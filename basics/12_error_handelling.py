#try except block

try:
    #if someone pass string as input then code will break, that is why we are using try except
    number = int(input("enter the numbers"))
    print(number)
    val = 10/0 # this error will also handele here
except:
    print("invalid number")

try:
    #if someone pass string as input then code will break, that is why we are using try except
    number = int(input("enter the numbers"))
    print(number)
    val = 10/0 # this error will also handele here
except ZeroDivisionError as err: #best practice is to use specific error
    print(err)
except ValueError:
    print("some other error")