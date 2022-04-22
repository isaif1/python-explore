monthConversion = {
    "Jan":"january",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sept":"September",
    "Oct":"October",
    "Nov": "November",
    "Dec":"December" 
}

print(monthConversion["Jan"])
print(monthConversion.get("Feb")) # if key is not present then will get None as value
print(monthConversion.get("Feb","Not a Valid Key")) # if key is not present then will get Not a Valid Key as value, if not present


#While Loop

i=1
while i<=10:
    print(i)
    i+=1


guess = ""
secret_word = "my_secret"
count=0

while guess !=secret_word and count <3:
    guess = input("Enter guess word");
    count+=1



#For Loop
for letter in "Girffe Academy":
    print(letter)#this will print in the next line

for index in range(3,10): #from 3 to 9
    print(index)


friends = ['hello', 'boys','readdy','boy']