#if we talk about python then we can store numbers string
name ='saif'

print(name)

#oh if you want quotation mark in your code then do this
print("hey this is saif\"how are you") #it will be like hey this is saif"how are you
#want something to write in the new line then
print("hey this is saif\nhow are you") 

# concatenation

print(name+" is cool")

full_name = "Saif Ali Ansari"

#there are some inbuilt functions
print(full_name.lower())
print(full_name.islower())

print(full_name.upper().isupper())#this will be true because same variable have been changed to upperCase

print(len(full_name))
#we can use index to access indexes of string

print(full_name[2])

#we can also get index of any string where it is starting from
#if something is not there then it will throw error
print(full_name.index("Al"))

#we can also replace some string to another string, it require two parameters
#it will return basically another string will not change in the same one
print(full_name.replace("Ali",""))
print(full_name)

